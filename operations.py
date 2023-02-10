# I am writing this program with the utmost effort and professionalilty?
# This file will contain all operations on music notes or sets of notes.

from info import notesFlat, notesSharp, naturalNotes, KeySignatures
import re

def identifyNoteType(note:str) -> str:
    # Does note contain 2+ chars?
    if len(note) >= 2:
        # What is the symbol at index 1?
        if note[1] == "b":
            return "flat"
        elif note[1] == "#":
            return "sharp"
    return "natural"

def transposeNote(note: str, semitones: int) -> str:
    if identifyNoteType(note) == "flat":
        return notesFlat[(notesFlat.index(note) + semitones) % len(notesFlat)]
    else:
        return notesSharp[(notesSharp.index(note) + semitones) % len(notesSharp)]

def findKey(notes: set):
    # Is valid notes? Do they follow the pattern T T s T T T s?

    # If set union of key and sig is equal to length of key given. All notes in key are in the signature. SO KEY IS POSSIBLE. However not enough info could be given to propose the exact key.
    keyPossibilities = []
    for sig in KeySignatures:
        sigNotes = set(KeySignatures[sig]["notes"])
        if len(sigNotes & notes) >= len(notes):
            keyPossibilities.append(sig)

    return keyPossibilities[0] if len(keyPossibilities) == 1 else keyPossibilities


# Iterate through the natural notes.
# If the note is not in the keysig, add it.
# If the note is in the keysig, add the note from the keysig. key is a list for ordering.

# def constructKey(tonic: str) -> list: # Tonic = root note (ie key name)
#     keySig = KeySignatures[tonic]["notes"] #Get notes in keysig
#     key = keySig.copy()
#     for naturalNote in naturalNotes:
#         if not list(filter(re.compile(f"{naturalNote}.").match, key)):
#             key.append(naturalNote)
#     # Key is in order where notes in keysig are first - Lets order it starting it where the tonic is. (tonic = key (root / 1))
#     # use sort func. Then we can cut the list where index(tonic) is and append it to the start.
#     key.sort()
#     tonicIndex = key.index(tonic)
#     key = key[tonicIndex:] + key[:tonicIndex]
#     return key

def noteAsNumber(note, key):
    keySig = KeySignatures[key]["notes"]
    return keySig.index(note) + 1