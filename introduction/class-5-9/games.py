from introduction.utils import logger
import divination
import foca


def start_game():
    logger.info('='*25)
    logger.info('   Select on Game!!!')
    logger.info('='*25)

    logger.info('(1) game name Divination, (2) game name Forca!')
    game_type = int(input())

    if game_type == 1:
        logger.info('-> Starting game Divination!')
        divination.start_game()
    elif game_type == 2:
        logger.info('-> Starting game Foca!')
        foca.start_game()


if __name__ == '__main__':
    start_game()
