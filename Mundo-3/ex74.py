from random import randrange
numbers = (randrange(1, 101), randrange(1, 101), randrange(1, 101), randrange(1, 101), randrange(1, 101))
print(numbers)
print(f'Maior: {max(numbers)} e Menor {min(numbers)}')