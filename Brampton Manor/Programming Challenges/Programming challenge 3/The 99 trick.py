def game():
    num1 = int(input("Select a number between 10-49: "))
    factor = 99 - num1

    num2 = int(input("Pick any number 50-99: "))
    add = str(num2 + factor)
    result = int(add[-2:]) + int(add[0])
    answer = num2 - result
    if answer == num1:
        print("I said the answer was {0} and the calculation result is {0}".format(num1))

if __name__ == "__main__" :
    game()
