import random

from introduction.utils import logger

attempts = 1
secret_number = random.randrange(1, 101)


def __get_level():
    logger.info('What level do you want? (1=Easy, 2=Medium, 3=Strong)')
    all_attempts = 0
    game_level = int(input())

    if game_level == 1:
        all_attempts = 20

    elif game_level == 2:
        all_attempts = 10

    elif game_level == 3:
        all_attempts = 5

    else:
        logger.error('Use the 1, 2 ou 3 on level game!')

    return all_attempts


def __execute_game(level):
    game_result = False
    points = 1000

    for attempts in range(1, level + 1):
        logger.info('You have attempts {} de {}: '.format(attempts, level))

        kick_str = input('Type the number!\n')
        logger.info('You type the number {}'.format(kick_str))

        kick = int(kick_str)
        right = kick == secret_number
        bigger = kick > secret_number
        less = kick < secret_number

        if kick < 1:
            logger.error('You must type number higher 1 and less 100!!!')
            continue

        if right:
            game_result = True
            logger.info('='*50)
            logger.info('Congratulation you have {:7.2f} points!!!'.format(points))
            logger.info('='*50)
            break
        else:
            if bigger:
                logger.info('You are wrong! The kick was higher than Secret number!!!')
            elif less:
                logger.info('You are wrong! The kick was less than Secret number!!!')
            lost_points = round(abs(secret_number - kick) /3) # 40 -20 = 20
            points = points - lost_points

        attempts += 1

    if not game_result:
        logger.warning('='*25)
        logger.warning('Gamer Over!!!')
        logger.warning('='*25)


def start_game():
    logger.info('-'*50)
    logger.info('- This is the Python3 Game, Welcome')
    logger.info('-'*50)

    __execute_game(__get_level())


if __name__ == '__main__':
    start_game()
