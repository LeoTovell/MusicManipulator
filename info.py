notesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
notesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
circleOfFithsSharp = ["C", "G", "D", "A", "E", "B", "F#", "C#", "Ab", "Eb", "Bb", "F"]
circleOfFithsFlat = ["C", "G", "D", "A", "E", "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F"]
naturalNotes = ["A", "B", "C", "D", "E", "F", "G"]
# allNotes = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
allNotes = ["A#", "B#", "C#", "D#", "E#", "F#", "G#", "Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "A", "B", "C", "D", "E", "F", "G"]
orderOfSharps = ["F#", "C#", "G#", "D#", "A#", "E#", "B#"]
orderOfFlats = ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]

regularKeyInterval = [2, 2, 1, 2, 2, 2, 1] # T T S T T T S

# Which keys contain what?
# Only contains the # or b

#https://en.wikipedia.org/wiki/Key_signature#Variants_of_standard_conventions

KeySignatures = {
    "C": {
        "notes": ["C", "D", "E", "F", "G", "A", "B"],
        "relative_minor": "Am",
        },
    "G": {
        "notes": ["G", "A", "B", "C", "D", "E", "F#"],
        "relative_minor": "Em",
        },
    "D": {
        "notes": ["D", "E", "F#", "G", "A", "B" "C#"],
        "relative_minor": "Bm",
        },
    "A": {
        "notes": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "relative_minor": "F#m",
        },
    "E": {
        "notes": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "relative_minor": "C#m",
        },
    "B": {
        "notes": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "relative_minor": "G#m",
        },
    "F#": {
        "notes": ["F#", "G#", "A#", "B", "C#", "D#" "E#"],
        "relative_minor": "D#m"
        },
    "C#": {
        "notes": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
        "relative_minor": "A#m"
        },
    "Cb": {
        "notes": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
        "relative_minor": "Abm"
        },
    "Gb": {
        "notes": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
        "relative_minor": "Ebm",
        },
    "Db": {
        "notes": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "relative_minor": "Bbm",
        },
    "Ab": {
        "notes": ["Ab", "Bb", "C", "Db", "Eb", "F", "C"],
        "relative_minor": "Fm",
        },
    "Eb": {
        "notes": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "relative_minor": "Cm",
        },
    "Bb": {
        "notes": ["Bb", "C", "D", "Eb", "F", "G", "A"],
        "relative_minor": "Gm",
        },
    "F" : {
        "notes": ["F", "G", "A", "Bb", "C", "D", "E"],
        "relative_minor": "Dm",
        },
}



if __name__ == "__main__":

    print("Here are all the notes which could be in a sharp key:", *notesSharp)
    print("Here are all the notes which could be in a flat key:", *notesFlat)

    [print(f"sharps in {key}: {vals['notes']}") for key, vals in KeySignatures.items()]