import random
from config import logs

LOG = logs.logger

LOG.info('-'*50)
LOG.info('- This is the Python3 Game, Welcome')
LOG.info('-'*50)

attempts = 1
secret_number = random.randrange(1, 101)


def get_level():
    LOG.info('What level do you want? (1=Easy, 2=Medium, 3=Strong)')
    all_attempts = 0
    game_level = int(input())

    if game_level == 1:
        all_attempts = 20

    elif game_level == 2:
        all_attempts = 10

    elif game_level == 3:
        all_attempts = 5

    else:
        LOG.error('Use the 1, 2 ou 3 on level game!')

    return all_attempts


def execute_game(level):
    game_result = False
    points = 1000

    for attempts in range(1, level + 1):
        LOG.info('You have attempts {} de {}: '.format(attempts, level))

        kick_str = input('Type the number!\n')
        LOG.info('You type the number {}'.format(kick_str))

        kick = int(kick_str)
        right = kick == secret_number
        bigger = kick > secret_number
        less = kick < secret_number

        if kick < 1:
            LOG.error('You must type number higher 1 and less 100!!!')
            continue

        if right:
            game_result = True
            LOG.info('='*50)
            LOG.info('Congratulation you have {:7.2f} points!!!'.format(points))
            LOG.info('='*50)
            break
        else:
            if bigger:
                LOG.info('You are wrong! The kick was higher than Secret number!!!')
            elif less:
                LOG.info('You are wrong! The kick was less than Secret number!!!')
            lost_points = round(abs(secret_number - kick) /3) # 40 -20 = 20
            points = points - lost_points

        attempts += 1

    if not game_result:
        LOG.warning('='*25)
        LOG.warning('Gamer Over!!!')
        LOG.warning('='*25)


def main():
    execute_game(get_level())


if __name__ == '__main__':
    main()
