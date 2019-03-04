from module1.utils import logger
import random


def start_game():
    logger.info('*'*50)
    logger.info('* This is the FOCA Game in Python3, Welcome')
    logger.info('*'*50)

    list_of_secrets_word = []
    with open('list-of-words.txt', 'r') as word_list:
        for line in word_list:
            line = line.strip().upper()
            list_of_secrets_word.append(line)

    number = random.randrange(0, len(list_of_secrets_word))
    secret_word = list_of_secrets_word[number]

    number = random.randrange(0, len(list_of_secrets_word))
    secret_word = list_of_secrets_word[number]

    the_correct_word = ["_" for word in secret_word]

    hang_himself = False
    winner = False
    errors = 0

    print('The secret word {} with size: {}'.format(the_correct_word, len(the_correct_word)))
    logger.warn(secret_word)

    while not winner and not hang_himself:
        option = input('What is the word?\n')
        option = option.strip().upper()

        if option in secret_word:
            index = 0
            for word in secret_word:
                if option.upper() == word.upper():
                    the_correct_word[index] = option
                index += 1
        else:
            errors += 1

        hang_himself = errors == 6
        winner = '_' not in the_correct_word
        print(the_correct_word)

    logger.info('-'*50)
    logger.info('The game is finished!!!')
    if winner:
        logger.info('Congratulation, you are the winner!!')
    else:
        logger.warn('OH MY GOOD, you are not winner!!')
    logger.info('-'*50)


if __name__ == '__main__':
    start_game()
