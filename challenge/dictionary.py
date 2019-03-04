dictionary = {}
for i in range(100):
    dictionary['name-{}'.format(i)] = 'value-{}'.format(i)

print(dictionary)