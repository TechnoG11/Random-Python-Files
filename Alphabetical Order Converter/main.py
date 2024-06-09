
#Function: orders a word into alphabetical order. "Cab" -> "abC"
def alphabetical(string):
    #Dict {a-z:1-26}
    A_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
           "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
           "Z": 26}

    new_string = []
    for i in range(len(string)):
        # Converts each letter into a number. "to" -> [[20, t], [15, o]]
        new_string.append([A_1[(string[(i)]).lower()], string[(i)]])
    new_string.sort()

    final_string = ""
    for i in range(len(new_string)):
        #Converts back to letters
        final_string += new_string[i][1]

    return final_string


# Output
print()
while True:
    print(alphabetical(input(">>")))
    print()