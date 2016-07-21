# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:36:50 2016

@author: jbraga
"""

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

dom = parse("just_gettin'_it.xml")

notes = dom.getElementsByTagName("note")
duration = dom.getElementsByTagName("duration")

#rests don't have steps or alters, so we don't care about them. Filter them out.
#notes = filter(lambda note: not is_rest(note), notes)

#compile a list of notes of all accidentals (notes with <alter> tags)
#accidentals = filter(is_accidental, notes)

#remove notes that are F or C
#accidentals_that_are_not_f_or_c = filter(lambda note: get_step(note) not in ["F", "C"], accidentals)

#compile a list of notes that don't contain the alter tag
#non_accidentals = filter(lambda note: not is_accidental(note), notes)

#remove notes that are not F or C
#non_accidentals_that_are_f_or_c = filter(lambda note: get_step(note) in ["F", "C"], non_accidentals)

#print "Accidental notes that are not F or C:"
#if len(accidentals_that_are_not_f_or_c) == 0:
#    print "(None found)"
#else:
#    for note in accidentals_that_are_not_f_or_c:
#        print get_step(note)
#
#print "Non-accidental notes that are F or C:"
#if len(non_accidentals_that_are_f_or_c) == 0:
#    print "(None found)"
#else:
#    for note in non_accidentals_that_are_f_or_c:
#        print get_step(note), get_step(note) in ["F", "C"]
        
print "NoteList:"
if len(notes) == 0:
    print "(None found)"
else:
    for note in notes:
        print get_step(note) + get_octave(note)
        print get_duration(note)
        
        
    