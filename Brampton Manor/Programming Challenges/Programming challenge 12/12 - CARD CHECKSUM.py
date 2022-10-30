def valid():
    num = input("Enter a card number ")
    if len(num) < 16:
        print("Number too short.")
        num = int(input("Enter a card number "))
    if len(num) > 16:
        print("Number too long.")
        num = int(input("Enter a card number "))

    try:
        int(num) * 2
    except TypeError:
        print("Card number must just be numbers.")
        num = int(input("Enter a card number "))

    return num


def pan(num):
    PAN = num[6:15]
    return PAN

def checksum(num):
    digit = num[-1]
    return digit

def issue(num):
    firstDigit = num[0]
    firstTwoDigits = num[0:1]
    if firstTwoDigits == "34" or firstTwoDigits == "37":
        print("American Express")
    elif firstTwoDigits == "51" or firstTwoDigits == "55":
        print("MasterCard")
    elif firstDigit == "3":
        print("JCB")
    elif firstDigit == "4":
        print("Visa")


def luhn(num):
    sum = 0
    length = len(num)
    if length%2 == 0:
        for i in range (length):
            if (i+1)%2 == 0:
                sum += int(num[i])
            else:
                sum += luhn2(int(num[i]))
    else:
        for i in range(length):
            if (i+1)%2 == 0:
                sum += luhn2(int(num[i]))
            else:
               sum += int(num[i]) 
    return sum%10

def luhn2(num):
    num = 2*int(num)
    if num>9:
        return num-9
    else:
        return num

if __name__ == "__main__":
    number = valid()
    p = pan(number)
    c = checksum(number)
    issue(number)
    if luhn(number) == 0:
        print("Card is valid")
