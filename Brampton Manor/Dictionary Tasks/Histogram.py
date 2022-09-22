def histogram():
    string = input("Enter a string. ")
    characters = []



    hist = {}
    sortedString = sorted(string)
    for i in sortedString:
        hist[i] = sortedString.count(i)


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
