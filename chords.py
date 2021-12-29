# chords takes key and mode as inputs and returns a list of all naturally occuring chords in that scale. 
# Currently only takes major or minor as input for mode.

def chords(key, mode):
    mode = mode.upper()
    key_ints = {"C":0, "C#":1, "Db":1, "D":2, "D#":3, "Eb":3, "E":4, "F":5, 
            "F#":6, "Gb":6, "G":7, "G#":8, "Ab":8, "A":9, "A#":10, "Bb":10, "B":11}
    keys = {0:"C", 1:"C#/Db", 2:"D", 3:"D#/Eb", 4:"E", 5:"F", 6:"F#/Gb", 7:"G", 8:"G#/Ab", 9:"A", 10:"A#/Bb", 11:"B"}
    
    key_int = key_ints[key]

    if mode == "MAJOR":
        chords = [0, 2, 4, 5, 7, 9, 11]
    elif mode == "MINOR":
        chords = [0, 2, 3, 5, 7, 8, 10]
    else: 
        print("mode error") # change this to an exception
        return

    for i in range(len(chords)):
        chords[i] = (chords[i] + key_int)%12
        chords[i] = keys[chords[i]]
    return chords


print(chords("C", "minor"))