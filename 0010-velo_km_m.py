"""Read a speed in km/h (kilometers per hour) and display it converted to m/s
(meters per second)."""

while True:
    try:
        value = float(input('Enter speed in kilometers: '))
        print(f"From {value} km/h to {round(value/3.6,4)} m/s.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
