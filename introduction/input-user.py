print('-'*50)
print('Welcome on my new Game!')
print('-'*50)

secret_number = 42
option_str = input('Type the number!: ')
option = int(option_str)

if option == secret_number:
    print('Correct!!!')
else:
    print('Wrong!!!')