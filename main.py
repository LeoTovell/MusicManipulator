from info import notesFlat, notesSharp
from operations import transposeNote

print("Here are all the notes which could be in a sharp key:", *notesSharp)
print("Here are all the notes which could be in a flat key:", *notesFlat)

print("note: A")

print(transposeNote("Ab", 5))