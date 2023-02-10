import sys
import os
import re

args = sys.argv[1:]

if len(args) < 1:
    raise Exception("No chordPro file supplied. Please supply a chordpro file as the argument.")

if len(args) > 1:
    raise Exception("Too many arguments. Try putting quotes around your chordPro filename.")

filepath = args[0]

if not os.path.isfile(filepath):
    raise FileNotFoundError("Invalid path: file not found")

# Start program.

print(os.path.split(filepath))

with open(filepath, "r") as f:
    lines = f.readlines()

def getMatchingBrackets(string):
    pairs = []
    currentPair = []
    open = False # State of algorithm (open bracket found) -> search for closed.
    for idx, char in enumerate(string):
        if not open:
            if char == "[":
                currentPair.append(idx)
                open = True
        else:
            if char == "]":
                currentPair.append(idx)
                pairs.append(currentPair)
                currentPair = []
                open = False
    
    return pairs

from info import allNotes

notesInLines = {}
songNotes = set()


for lineIndex, line in enumerate(lines):
    line = line.strip()
    
    # does line contains a set of []
    if "[" in line and "]" in line:
        notesInLines[lineIndex] = []
        pairs = getMatchingBrackets(line)
        for pair in pairs:
            note = line[pair[0] + 1 : pair[1]]
            # Parse if the note is in an instrumental/tag or something similiar : ie (| D /// Eadd4/D // F#m /// E // E/A // |)
            # Parse for EaddX later.
            # print(note)
            for n in allNotes:
                if n in note:
                    notesInLines[lineIndex].append({"note": n, "indexStart": line.index(n), "indexStop": line.index(n) + len(n)})
                    note = note[:note.index(n)] + note[note.index(n) + len(n):]
            
        # Get all notes from the whole chordPro (fingers crossed no keychange)
        for note in notesInLines[lineIndex]:
            songNotes.add(note["note"])

from operations import findKey, noteAsNumber

songKey = findKey(songNotes)

noteConversion = {note: noteAsNumber(note, songKey) for note in songNotes}

newLines = []

for lineIndex, line in enumerate(lines):
    if not notesInLines.get(lineIndex):
        newLines.append(line)
    else:
        # sort the note array so we can do them back to front to avoid messing up existing index numbers!
        sortedList = sorted(notesInLines[lineIndex], key=lambda x: x["indexStart"])
        sortedList.reverse()
        for note in sortedList:
            number = str(noteAsNumber(note["note"], songKey))
            startIndex = note["indexStart"]
            stopIndex = note["indexStop"]
            line = line[:startIndex] + number + line[startIndex + len(number):] # irrelevant as length of number will always be 1.
        newLines.append(line)

head, tail = os.path.split(filepath)
newFilepath = os.path.join(head, f"NUMBERS - {tail}") 

with open(newFilepath, "w") as f:
    for line in newLines:
        f.write(line)