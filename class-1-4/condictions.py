print('-'*50)
print('Welcome on my new Game!')
print('-'*50)

secret_number = 42
option_str = input('Type the number!: ')
option = int(option_str)

correct = option == secret_number
higher = option > secret_number
lower = option < secret_number

if correct:
    print('Correct!!!')
else:
    print('Wrong!!!')
    if higher:
        print('Your number is higher than Secret Number!')
    elif lower:
        print('Your number is lower than Secret Number!')

