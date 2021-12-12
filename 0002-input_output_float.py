# Enter a number and print the floating value.

while True:
    try:
        value = float(input('Enter a number: '))
        print(f'The entered number is {value}.')
        if value == 0:
            break
    except:
        print('The number must be an integer.')
        continue
