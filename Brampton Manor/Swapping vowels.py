string = input("Enter a string. ")
strlength = len(string)

vowels = ["a", "e", "i", "o", "u"]
dictionary = {}
for i in range(0,strlength):
    if string[i] in vowels:
        dictionary[i] = string[i]

newString = []
sort = sorted(dictionary.keys(),reverse=True)
x = 0
for i in range(0,strlength):
    if i in dictionary:
        newString.append(string[sort[x]])
        x += 1
    else:
        newString.append(string[i])

print("".join(newString))

