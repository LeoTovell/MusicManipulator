from info import notesFlat, notesSharp, KeySignatures
from operations import transposeNote

print("Here are all the notes which could be in a sharp key:", *notesSharp)
print("Here are all the notes which could be in a flat key:", *notesFlat)

print("note: A")

print(transposeNote("Ab", 5))

print("key sigs\n")

[print(f"sharps in {key}: {vals['notes']}") for key, vals in KeySignatures.items()]
# for i in KeySignatures:
