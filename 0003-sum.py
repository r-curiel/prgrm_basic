# Ask the user to enter three integer values and print their sum.

while True:
    try:
        total = sum([int(input(f'Enter a number {x + 1}/3: ')) for x in range(3)])
        if total == 0:
            break
        else:
            print(total)
    except:
        print('Invalid value, re-enter numbers.')
        continue
