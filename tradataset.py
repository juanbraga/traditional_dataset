# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 20:28:46 2016

@author: Juan
"""

import numpy as np
import scipy.io.wavfile as wav
import csv

def load_list():

    ltrdataset=[]    
    cr = csv.reader(open('../traditional_dataset/dataset.csv',"rb"))
    for row in cr:
        ltrdataset.append(row[0]) 
        
    return ltrdataset
    
def load_gt(gt_file, t):
    
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
    
    return vad_gt
    
def load_audio(audio_file):
    
    fs, audio = wav.read(audio_file)
#    audio = audio.astype('float64')
    t = np.arange(len(audio)) * float(1)/fs
    
    return audio, t, fs  
    
    
tdlist = load_list()