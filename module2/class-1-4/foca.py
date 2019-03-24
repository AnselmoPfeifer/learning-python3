from module1.utils import logger


def start_game():
    logger.info('*'*50)
    logger.info('* This is the FOCA Game in Python3, Welcome')
    logger.info('*'*50)
    print()

    the_correct_word = ['_', '_', '_', '_', '_', '_']
    secret_word = 'banana'
    hang_himself = False
    hit = False
    print('The secret word {} with size: {}'.format(the_correct_word, len(the_correct_word)))

    while not hit and not hang_himself:
        option = input('What is the word?\n')
        option = option.strip()
        index = 0

        for word in secret_word:
            if option.upper() == word.upper():
                the_correct_word[index] = option
            index = index + 1
        print(the_correct_word)

    logger.info('-'*50)
    logger.info('The game is finished!!!'.ca)
    logger.info('-'*50)


if __name__ == '__main__':
    start_game()
