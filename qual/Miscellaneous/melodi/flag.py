from mido import MidiFile
import os

folder = "chall"
total_sum = 0

for f in os.listdir(folder):
    if f.endswith(".mid"):
        mid = MidiFile(os.path.join(folder, f))
        notes = []

        for msg in mid.tracks[0]:
            if msg.type == 'note_on' and msg.velocity > 0:
                notes.append(msg.note)

        if notes:
            product = 1
            for n in notes:
                product *= n
            total_sum += product

digit_str = str(total_sum)
pitches = [int(digit_str[i:i+2]) for i in range(0, len(digit_str)-1, 2)]

# Step 3: Konversi ke not musik
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def convert_pitchtonotes(pitch):
    octave = pitch // 12 - 1
    note = notes[pitch % 12]
    return f"{note}{octave}"

notes = [convert_pitchtonotes(p) for p in pitches]

print("".join(notes))
