# This program outputs a list of naturally occurring chords in any given major or natural minor scale. 
# It is based on music theory, and it is a useful tool for music composition.
# Author: Andrew Luther
# Version: Dec 29 2021

def chords(key, mode):
    mode = mode.upper()
    key_ints = {"C":0, "C#":1, "Db":1, "D":2, "D#":3, "Eb":3, "E":4, "F":5, 
            "F#":6, "Gb":6, "G":7, "G#":8, "Ab":8, "A":9, "A#":10, "Bb":10, "B":11}
    keys = {0:"C", 1:"C#/Db", 2:"D", 3:"D#/Eb", 4:"E", 5:"F", 6:"F#/Gb", 7:"G", 8:"G#/Ab", 9:"A", 10:"A#/Bb", 11:"B"}
    
    key_int = key_ints[key]

    if mode == "MAJOR":
        chords = [[0, 0], [2, 1], [4, 1], [5, 0], [7,0], [9,1], [11,2]] # 0 is maj 1 is min 2 is dim
    elif mode == "MINOR":
        chords = [[0, 1], [2, 2], [3, 0], [5, 1], [7,1], [8,0], [10,0]]
    else: 
        print("Invalid Input")
        return

    for i in range(len(chords)):
        chords[i][0] = (chords[i][0] + key_int)%12
        chords[i][0] = keys[chords[i][0]]
        if chords[i][1] == 0: chords[i][1] = "major"
        elif chords [i][1] == 1: chords[i][1] = "minor"
        elif chords [i][1] == 2: chords[i][1] = "diminished"
    return chords

def main():
    print(chords("G", "minor"))

if __name__ == "__main__":
    main()

