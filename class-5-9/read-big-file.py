from config import logs

LOG = logs.logger

input_file = open('big.txt', 'r')
output_file = open('output.txt', 'w')

LOG.info('reading the first 500 lines the big file !!!')
for lines in range(500):
    line = input_file.readline()
    output_file.write(line)
LOG.info('wrote 500 lines on new file !!!')

################################################################
LOG.info('reading the big file !!!')
while 1:
    for lines in range(100):
        LOG.info(input_file.readline())

################################################################

filepath = 'big.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        LOG.info("line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
