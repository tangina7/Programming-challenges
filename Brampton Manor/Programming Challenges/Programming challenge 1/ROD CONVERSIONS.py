
distance = float(input("Enter the distance in rods. "))
print(distance, "rods")

def Metres(distance):
    metres = distance * 5.0292
    print(metres, "metres")

def Furlongs(distance):
    furlongs = distance / 40
    print(furlongs, "furlongs")

def Miles(distance):
    miles = (distance * 5.0292) / 1609.34
    print(miles, "miles")
    return miles

def Feet(distance):
    feet = (distance * 5.0292) / 0.3048
    print(feet, "feet")

def Time(distance):
    miles = (distance * 5.0292) / 1609.34
    average = miles / 3.1
    time = average * 60
    print("The time taken to walk that distance in minutes is", time)

Time(distance)
Feet(distance)
Miles(distance)
Furlongs(distance)
Metres(distance)
