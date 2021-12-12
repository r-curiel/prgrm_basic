"""Read a temperature in degrees Celsius and display it converted to degrees Fahrenheit.
The conversion formula is: F = C*(9.0/5.0)+32.0, where F is the temperature in Fahrenheit
and C is the temperature in Celsius."""

while True:
    try:
        value = float(input('Enter the Celsius temperature: '))
        print(f"From {value}ºC to {(value * (9.0/5.0)+32)}ºF.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
