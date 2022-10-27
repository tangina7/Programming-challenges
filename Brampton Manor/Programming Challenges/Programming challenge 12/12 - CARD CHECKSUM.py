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
    parity = length % 2
    for i in range (0,length):
       n = (str(num))[i]
       n = int(n)
       if i % 2 == parity:
          sum = sum + n
       elif n > 4:
          sum = sum + (2*n) - 9
       else:
          sum = sum + (2*n)
    if sum % 10 == 0:
        return sum

if __name__ == "__main__":
    number = valid()
    p = pan(number)
    c = checksum(number)
    issue(number)
    l = luhn(number)
