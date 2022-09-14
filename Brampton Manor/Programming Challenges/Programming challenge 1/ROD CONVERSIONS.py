distance = float(input("Enter the distance in rods. "))
print("Your input {} rods".format(distance))

def Metres(distance):
    metres = distance * 5.0292
    return metres

def Furlongs(distance):
    furlongs = distance / 40
    return furlongs

def Miles(distance):
    miles = (distance * 5.0292) / 1609.34
    return miles

def Feet(distance):
    feet = (distance * 5.0292) / 0.3048
    return feet

def Time(distance):
    miles = (distance * 5.0292) / 1609.34
    average = miles / 3.1
    time = average * 60
    return time


def run():
    print("\n" + "Conversions")
    print("Metres: {}".format(Time(distance)))
    print("Feet: {}".format(Feet(distance)))
    print("Miles: {}".format(Miles(distance)))
    print("Furlongs: {}".format(Furlongs(distance)))
    print("Minutes to walk {} rods: {}".format(distance,Time(distance)))


if __name__ == "__main__":
    run()
