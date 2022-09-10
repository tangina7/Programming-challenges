def values():
    txt = "Richter {:<16} Joules {:<17} TNT".format(" ", " ")
    print(txt)

    earthquake = [1.0, 5.0, 9.1, 9.2, 9.5]
    for i in earthquake:
        energy = 10**((1.5*i)+4.8)
        tnt = energy / (4.184*10**9)
        print("{:<24} {:<24} {}".format(i, energy, tnt))

def calc():
    print("\n")
    richter = float(input("Please enter a Richter scale measurement. "))
    print("Richter scale {}".format(richter))
    energy = 10**((1.5*richter)+4.8)
    tnt = energy / (4.184*10**9)
    print("Equivalence in joules: {}".format(energy))
    print("Equivalence in tons of TNT: {}".format(tnt))


if __name__ == "__main__":
    values()
    calc()
