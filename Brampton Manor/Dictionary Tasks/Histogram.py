def histogram():
    string = input("Enter a string. ")
    characters = []
    
    for letter in string:
        characters.append(letter)
    length = len(characters)


    hist = {}
    for i in characters:
        freq = 0
        for x in range(0,length):
            if i == characters[x]:
                freq += 1
                hist[i] = freq
                

        
    dictLength = len(hist)
    for y in range (0, dictLength):
        keysList = list(hist.keys())
        key = keysList[y]

        if hist[key] > 1:
            ending = "times"
        else:
            ending = "time"
        print("The letter {} appears {} {}".format(key, hist[key], ending))


 
if __name__ == "__main__":
    histogram()

