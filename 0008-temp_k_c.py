"""Read a temperature in degrees Kelvin and display it converted to degrees Celsius.
Conversion formula is: C = K - 273.15, where C is the temperature in Celsius and K is
temperature in Kelvin."""

while True:
    try:
        value = float(input('Enter the Kelvin temperature: '))
        print(f"From {value}ºK to {round(value - 273.15, 2)}ºC.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
