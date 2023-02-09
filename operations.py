# I am writing this program with the utmost effort and professionalilty?
# This file will contain all operations on music notes or sets of notes.

from info import notesFlat, notesSharp

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