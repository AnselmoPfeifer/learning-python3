from module1.utils import logger
import random


def start_message():
    logger.info('*'*50)
    logger.info('* This is the FOCA Game in Python3, Welcome')
    logger.info('*'*50)


def end_message(winner):
    lost = """
                ______________
              /               \      
             /                 \     
          //                   \/\ 
          \|   XXXX     XXXX   | /  
            |   XXXX     XXXX   |/ 
            |   XXX       XXX   |   
            |                   |  
             \__      XXX      __/     
              |\     XXX     /|       
              | |           | |        
              | I I I I I I I |        
              |  I I I I I I  |       
              \_             _/       
               \_         _/         
                 \_______/           
    """
    logger.info('The game is finished!!!')
    if winner:
        logger.info('Congratulation, you are the winner!!!')
    else:
        logger.error('OH MY GOOD, you are not winner!!')
        logger.error(lost)


def read_file():
    list_of_secrets_word = []
    with open('list-of-words.txt', 'r') as word_list:
        for line in word_list:
            line = line.strip().upper()
            list_of_secrets_word.append(line)

    number = random.randrange(0, len(list_of_secrets_word))
    secret_word = list_of_secrets_word[number].upper().strip()
    return secret_word


def hidden_letter(word):
    return ['_' for letter in word]


def start_game(word):
    the_correct_word = hidden_letter(word)

    hang_himself = False
    winner = False
    errors = 0

    print('The secret word {} with size: {}'.format(the_correct_word, len(the_correct_word)))
    logger.warn(word)

    while not hang_himself and not winner:
        option = input('What is the word?\n')
        option = option.strip().upper()

        if option in word:
            index = 0
            for letter in word:
                if option == letter:
                    the_correct_word[index] = option
                index += 1
        else:
            errors += 1

        hang_himself = errors == 6
        winner = '_' not in the_correct_word
        print(the_correct_word)
    return winner


if __name__ == '__main__':
    secret_word = read_file()
    start_message()
    winner = start_game(secret_word)
    end_message(winner)
