from pyknon.music import Note
from pyknon.music import NoteSeq
from pyknon.music import Rest
from pyknon.genmidi import Midi


C_note = Note(0, 5, dur=0.25) 
A_note = Note(9, 5, 0.25)
quarter_rest = Rest(0.25) # quarter rest

# create a sequence of notes and rests
seq = NoteSeq([C_note, A_note, quarter_rest, C_note]) 

midi = Midi(1, tempo=120)
midi.seq_notes(seq, track=0)
midi.write("simple_noteseq.mid")