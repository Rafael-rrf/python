from random import randrange
num = randrange(0, 6)
num2 = int(input('Digite um númnero de 0 a 5: '))
print(num)
if num == num2:
    print('Você acertou!!')

else:
    print(f'Você errou, o computador escolheu o número {num} ')