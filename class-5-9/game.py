import random
from config import logs

LOG = logs.logger

LOG.info('-'*50)
LOG.info('- This is the Python3 Game, Welcome')
LOG.info('-'*50)

secret_number = random.randrange(1, 101)
all_attempts = 3
attempts = 1
game_result = False

for attempts in range(1, all_attempts + 1):
    LOG.info('You have attempts {} de {}: '.format(attempts, all_attempts))

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
        LOG.info('You are right!!!')
        LOG.info('='*50)
        break
    else:
        if bigger:
            LOG.info('You are wrong! The kick was higher than Secret number!!!')
        elif less:
            LOG.info('You are wrong! The kick was less than Secret number!!!')

    attempts += 1


if not game_result:
    LOG.warning('='*25)
    LOG.warning('Gamer Over!!!')
    LOG.warning('='*25)
