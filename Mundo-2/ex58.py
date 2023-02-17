from random import randrange
cont = 1
num = int(input('Digite um número: '))
numGerado = randrange(1, 11)
while num != numGerado:
    num = int(input('Você errou, tente novamente: '))
    cont += 1
print(f'Você acertou, foram necessárias {cont} tentativas')