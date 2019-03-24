my_file = open('2-list-of-words.txt', 'w')
print(my_file)
# <_io.TextIOWrapper name='list-of-words.txt' mode='w' encoding='UTF-8'>
my_file.write('Python')
my_file.close()

# The same action we can use with to open and read / write a file.
with open('2-list-of-words.txt', 'w') as words_file:
    words_file.write('Python Tonic')

# The same action we can use with to open and read / write a file.
with open('list-of-words.txt', 'r') as words_file:
    print(words_file.readline())
