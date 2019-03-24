# Example of the list interaction using comprehensions
squares = [x * x for x in range(10)]
print('{}'.format(squares))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example of the list interaction simple loop
squares = []
for x in range(10):
    squares.append(x * x)
print('{}'.format(squares))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example of the list interaction using comprehensions
# Get even squares
even_squares = [x * x for x in range(10) if x % 2 == 0 if x * x == 16]
print('{}'.format(even_squares))
# [16]

# Example of the list interaction simple loop
# Get even squares
even_squares = []
value = False
for x in range(10):
    if x % 2 == 0 and x * x == 16:
        even_squares.append(x * x)
print('{}'.format(even_squares))
# [16]

inteiros = [1, 3, 4, 5, 7, 8, 9]
pares = [n % 2 for n in inteiros]
print(pares)
# [4, 8]

pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
    print(pares)
# [4, 8]