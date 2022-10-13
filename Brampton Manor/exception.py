import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

symbol = input("Enter a symbol. ")
num = int(input("Enter a natural number. "))



print(f'{symbol}  | ', end = "")
for i in range (0,num+1):
    print('{} {:>2}'.format(i," "), end = "")
print()
print("-"*num*5)


for i in range (0,num):
    print(f'{i}  | ', end = "")
    for j in range(0,num+1):
        print("{} {:<2}".format(ops[symbol](i,j), " "), end = "")
    print()
