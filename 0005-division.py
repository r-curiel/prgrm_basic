# Read a real number and print the fifth part of that number.

while True:
    try:
        value = int(input('Enter a number: '))
        print(f"The fifth part of {value} is {value / 5}.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue