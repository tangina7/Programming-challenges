def values(temp,speed):
    windChill = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16
    return windChill

def user():
    temp = float(input("Temperature: "))
    speed = float(input("Speed: "))
    windChill = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16
    return windChill

def run():
    statement = "Temperature of {} and speed of {} gives windchill of:"
    print(statement.format(10,15), values(10,15))
    print(statement.format(0.0,25), values(0.0,25))
    print(statement.format(-10,35), values(-10,35))
    print("Windchill:",user())


if __name__ == "__main__":
          run()
