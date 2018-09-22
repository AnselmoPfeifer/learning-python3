from introduction.utils import logger

data_list = ['test', 'test1', 'test2', 'test2']


def read_file():
    logger.info('read the big file!!!')
    try:
        with open('big.txt', 'r') as big:
            text = big.read()
        return text
    except FileNotFoundError:
        logger.error('file not exist!!!')


def write_file():
    try:
        with open('new_file.txt', 'w') as new_file:
            for line in data_list:
                new_file.write(line)
                new_file.write('\n')

        with open('new_file.txt', 'a') as new_file:
            print(23*'=', file=new_file)
            print('this is the new content file', file=new_file)

    except IOError:
        logger.error('error to write the new file!!!')


read_file()
write_file()
