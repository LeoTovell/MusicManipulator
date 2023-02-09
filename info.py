notesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
notesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
circleOfFithsSharp = ["C", "G", "D", "A", "E", "B", "F#", "C#", "Ab", "Eb", "Bb", "F"]
circleOfFithsFlat = ["C", "G", "D", "A", "E", "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F"]

regularKeyInterval = [2, 2, 1, 2, 2, 2, 1] # T T S T T T S

# Which keys contain what?
# Only contains the # or b

#https://en.wikipedia.org/wiki/Key_signature#Variants_of_standard_conventions

KeySignatures = {
    "C": {
        "notes": [],
        "relative_minor": "Am",
        },
    "G": {
        "notes": ["F#"],
        "relative_minor": "Em",
        },
    "D": {
        "notes": ["F#", "C#"],
        "relative_minor": "Bm",
        },
    "A": {
        "notes": ["F#", "C#", "G#"],
        "relative_minor": "F#m",
        },
    "E": {
        "notes": ["F#", "C#", "G#", "D#"],
        "relative_minor": "C#m",
        },
    "B": {
        "notes": ["F#", "C#", "G#", "D#", "A#"],
        "relative_minor": "G#m",
        },
    "F#": {
        "notes": ["F#", "C#", "G#", "D#", "A#", "E#"],
        "relative_minor": "D#m"
        },
    "C#": {
        "notes": ["F#", "C#", "G#", "D#", "A#", "E#", "B#"],
        "relative_minor": "A#m"
        },
}