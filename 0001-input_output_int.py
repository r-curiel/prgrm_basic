# A program that receive a number and return it

while True:
    try:
        value = int(input('Enter a number: '))
        print(f'The entered number is {value}.')
        if value == 0:
            break
    except:
        print('The number must be an integer.')
        continue
