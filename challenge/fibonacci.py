from functools import lru_cache

fibonacci_cache = {}


@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError('n must be a positive int!!!')

    if n < 1:
        raise TypeError('n must be a positive int!!!')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n -1) + fibonacci(n -2)


for n in range(1, 501):
    print('{} : {}'.format(n, fibonacci(10)))


def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n -1) + fibonacci(n -2)

numbers = []
for n in range(10):
    numbers.append(fibonacci(n))

numbers = set(numbers)
numbers = list(numbers)
print(numbers)
