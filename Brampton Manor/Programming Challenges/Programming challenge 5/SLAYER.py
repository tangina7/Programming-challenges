def calc(slayer):
    total = slayer * 3
    slayer = str(slayer)
    layers = int(slayer[1:] + slayer[0])
    return layers,total

def game():
    print("Guess a six-digit number SLAYER so that following equation is true, "
          "where each letter stands for the digit in the position shown:"
          " SLAYER + SLAYER + SLAYER = LAYERS")
    s = int(input("Enter your guess for SLAYER: "))
    layers,total = calc(s)
    if total == layers:
        print("Your guess is correct:")
    else:
        print("Your guess is incorrect:")
    print("SLAYER + SLAYER + SLAYER = ",total)
    print("LAYERS = ",layers)
    print("Thanks for playing.")

if __name__ == "__main__":
    game()
