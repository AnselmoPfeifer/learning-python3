print('-'*50)
print('This is the Python3 Game', 'Welcome', sep=' - ', end="\n" + '-'*50 + '\n')

secret_number = 42
all_attempts = 3
attempts = 1

while attempts <= all_attempts:
    print('You have attempts {} de {}: '.format(attempts, all_attempts))
    kick_str = input('Type the number!')
    print('You type the number %s' % kick_str)
    kick = int(kick_str)

    right = kick == secret_number
    bigger = kick > secret_number
    less = kick < secret_number

    if right:
        print('-'*50)
        print('You are right!!!')
        print('-'*50)
        break
    else:
        if bigger:
            print('You are wrong! The kick was higher than Secret number!!!')
        elif less:
            print('You are wrong! The kick was less than Secret number!!!')

    attempts += 1

