# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 20:28:46 2016

@author: Juan
"""
import librosa as lr
import numpy as np
import scipy.io.wavfile as wav
import csv
from xml.dom.minidom import parse, parseString

def get_step(note):
    stepNode = note.getElementsByTagName("step")[0]
    #get the text from the Text Node within the <step>,
    #and convert it from unicode to ascii
    return str(stepNode.childNodes[0].nodeValue)
    
def get_duration(note):
    noteDuration = note.getElementsByTagName("duration")[0]
    #get the text from the Text Node within the <duration>,
    #and convert it from unicode to ascii
    return str(noteDuration.childNodes[0].nodeValue)
    
def get_octave(note):
    noteOctave = note.getElementsByTagName("octave")[0]
    #get the text from the Text Node within the <octave>,
    #and convert it from unicode to ascii
    return str(noteOctave.childNodes[0].nodeValue)

def get_alter(note):
    alters = note.getElementsByTagName("alter")
    if len(alters) == 0:
        return None
    alters = note.getElementsByTagName("alter")[0]
    return str(alters.childNodes[0].nodeValue)

def is_rest(note):
    return len(note.getElementsByTagName("rest")) > 0

def is_accidental(note):
    return get_alter(note) != None
    
def is_fermata(note):
    return len(note.getElementsByTagName("fermata")) > 0
    
def is_grace(note):
    return len(note.getElementsByTagName("grace")) > 0
    
def load_score(score_file):

    dom = parse(score_file)

    xml_notes = dom.getElementsByTagName("note")
    
    notes=[]
    durations=[]
    contador=0
    for note in xml_notes:
        contador = contador + 1
        if is_fermata(note):
            print 'fermata'
        if is_grace(note):
            durations.append('0')
            #print 'grace note'
        else:
            durations.append(get_duration(note))
        if is_rest(note):
            notes.append('0')
        else: 
            if is_accidental(note):
                alter_aux = get_alter(note)
                if alter_aux == '1':
                    notes.append(get_step(note) + '#' + get_octave(note))
                if alter_aux == '2':
                    notes.append(get_step(note) + '##' + get_octave(note))
                if alter_aux == '-1':
                    notes.append(get_step(note) + 'b' + get_octave(note))
                if alter_aux == '-2':
                    notes.append(get_step(note) + 'bb' + get_octave(note))
            else:
                notes.append(get_step(note) + get_octave(note))
       
    durations=np.array(durations,dtype='int16')
    
    cr = csv.reader(open("../traditional_dataset/note_convertion.csv","rb"))
          
    notation=[]
    frequency=[]
    
    for row in cr:
    
        notation.append(row[0]) 
        frequency.append(row[1])
    
    frequency = np.array(frequency, 'float64')
    
    i=0
    melo = np.empty([0,])
    for note in notes:
        if note=='0':
            for k in range(0,durations[i]):            
                melo = np.r_[melo,0]
        else:
            for k in range(0,durations[i]):            
                melo = np.r_[melo,frequency[notation.index(note)]]
        i=i+1
    
    
    score = lr.hz_to_midi(melo)
    np.place(score,score==-np.inf,0)
    return score, notes
    
def modify_score():
    pass

def load_list():

    ltrdataset=[]    
    cr = csv.reader(open('../traditional_dataset/dataset.csv',"rb"))
    for row in cr:
        ltrdataset.append(row[0]) 
        
    return ltrdataset
    
def load_gt(gt_file, t, fs = 44100, frame=1024, hop=1024):
    
    cr = csv.reader(open(gt_file,"rb"))
    onset=[]
    notes=[]
    for row in cr:
        onset.append(row[0]) 
        notes.append(row[1])
    onset = np.array(onset, 'float32')
    
    aux_vad_gt = np.empty([0,], 'int8')
    for note in notes:
        if note=='0':
            aux_vad_gt = np.r_[aux_vad_gt,0]
        else:
            aux_vad_gt = np.r_[aux_vad_gt,1]
    
    j=0
    vad_gt = np.empty([len(t),], 'int8')
    for i in range(1,len(onset)):
        while (j<len(t) and t[j]>=onset[i-1] and t[j]<=onset[i]):
            vad_gt[j]=aux_vad_gt[i-1]
            j=j+1
    
    cr = csv.reader(open("./traditional_dataset/note_convertion.csv","rb"))
          
    notation=[]
    frequency=[]
    
    for row in cr:
    
        notation.append(row[0]) 
        frequency.append(row[1])
    
    frequency = np.array(frequency, 'float64')
    
    i=0
    melo = np.empty([0,])
    for note in notes:
        if note=='0':
            melo = np.r_[melo,0]
        else:
            melo = np.r_[melo,frequency[notation.index(note)]]
        i=i+1
        
    j=0
    t_aux = np.arange(len(t)/1024 - 1) * float(hop)/fs     
    
    gt_aux = np.empty([len(t_aux),],'float64')
    for i in range(1,len(onset)):
        while (j<len(t_aux) and (t_aux[j])>=onset[i-1] and (t_aux[j])<=onset[i]):
            gt_aux[j]=melo[i-1]
            j=j+1
    
    
    #gt_aux = lr.hz_to_midi(gt_aux)
    #np.place(gt_aux,gt_aux==-np.inf,0)
    
    return vad_gt, gt_aux, onset, melo
        
    
def load_audio(audio_file):
    
    fs, audio = wav.read(audio_file)
    audio = audio.astype('float32')
#    audio = audio.astype('float64')
    t = np.arange(len(audio)) * float(1)/fs
    
    return audio, t, fs  


def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("node does not contain text")

    node.firstChild.replaceWholeText(newText)    
    
if __name__=="__main__":

    ltrdataset = load_list()    

    fragment = ltrdataset[9]    

    audio_file = fragment + '_mono.wav'
    gt_file = fragment + '.csv'
    score_file = fragment + '.xml'

    audio, t, fs = load_audio(audio_file)
    activity_gt, notes_gt, onset_gt, melodiii = load_gt(gt_file, t)       
    score, notes = load_score(score_file)

#    dom = parse("just_gettin'_it.xml")
#
#    xml_notes = dom.getElementsByTagName("note")
#    
#    for note in xml_notes:
#        node = note.getElementsByTagName("duration")[0]
#        replaceText(node, '10')
#    
#    import codecs
#    with codecs.open('edited.xml','w', encoding="utf-8") as f:
#        f.write(dom.toxml(),)