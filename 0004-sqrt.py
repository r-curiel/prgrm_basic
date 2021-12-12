# Read a real number and print the square result of that number.

import math

while True:
    try:
        value = int(input('Enter a number: '))
        print(f"The square root of {value} is {round((math.sqrt(value)), 2)}.")
        if value == 0:
            break
    except:
        print('Invalid value, re-enter numbers.')
        continue
