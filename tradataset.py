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
        return ' '
    return alters[0]

def is_rest(note):
    return len(note.getElementsByTagName("rest")) > 0

def is_accidental(note):
    return get_alter(note) != None
    
def load_score(score_file):

    dom = parse(score_file)

    xml_notes = dom.getElementsByTagName("note")
    
    notes=[]
    durations=[]
    for note in xml_notes:
        if is_rest(note):
            notes.append('0')
            durations.append(get_duration(note))
        else:
            notes.append(get_step(note) + get_octave(note))
            durations.append(get_duration(note))
        
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
    return score

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
            melo = np.r_[melo,0]
        else:
            melo = np.r_[melo,frequency[notation.index(note)]]
        i=i+1
        
        j=0

    t = np.arange(len(t)/1024 - 1) * float(hop)/fs     
    
    gt = np.empty([len(t),],'float64')
    for i in range(1,len(onset)):
        while (j<len(t) and (t[j])>=onset[i-1] and (t[j])<=onset[i]):
            gt[j]=melo[i-1]
            j=j+1
    
    
    gt = lr.hz_to_midi(gt)
    np.place(gt,gt==-np.inf,0)
    return vad_gt, gt, onset
        
    
def load_audio(audio_file):
    
    fs, audio = wav.read(audio_file)
#    audio = audio.astype('float64')
    t = np.arange(len(audio)) * float(1)/fs
    
    return audio, t, fs  
    
    
if __name__=="__main__":
    
    score=load_score(score_file)