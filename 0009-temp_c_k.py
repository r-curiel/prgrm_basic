"""Read a temperature in degrees Celsius and display it converted to degrees Kelvin. A
Conversion formula is: K = C + 273.15, where C is the temperature in Celsius and K is
temperature in Kelvin."""

while True:
    try:
        value = float(input('Enter the Celcius temperature: '))
        print(f"From {value}ºC to {round(value + 273.15, 2)}ºK.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
