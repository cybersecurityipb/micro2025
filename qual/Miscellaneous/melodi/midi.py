import os
import random
import string
from mido import Message, MidiFile, MidiTrack

hex_str = ''.join(random.choices('0123456789abcdef', k=100000))

chunks = [hex_str[i:i+10] for i in range(0, len(hex_str), 10)]

def convert_hextopitch(hex_chunk):
    pitches = []
    for i in range(0, len(hex_chunk), 2):
        val = int(hex_chunk[i:i+2], 16)
        pitch = (val % 49) + 60 
        if pitch % 2 != 0:
            pitch += 1
        if pitch > 108:
            pitch -= 2
        pitches.append(pitch)
    return pitches

def rand_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

os.makedirs("chall", exist_ok=True)

for chunk in chunks:
    pitches = convert_hextopitch(chunk)
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=0, time=0))
    
    for note in pitches:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=480))

    filename = f"chall/{rand_name()}.mid"
    mid.save(filename)

