"""Read a temperature in degrees Fahrenheit and display it converted to degrees Celsius.
The conversion formula is: C = 5.0* (F - 32.0)/9.0, where C is the temperature in Celsius
and F is the temperature in Fahrenheit."""

while True:
    try:
        value = float(input('Enter the Fahrenheit temperature: '))
        print(f"From {value}ºF to {round(5.0 * (value - 32)/9.0, 2)}ºC.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
