from random import randrange
count = 0
while True:
    botNumber = randrange(0, 6)
    userNumber = int(input('Digite um número:'))
    choice = int(input('Par ou Ímpar ? 1- Par  2- Impar'))
    sum = botNumber + userNumber
    print(f'O computador escolheu o número: {botNumber}')
    print(f'O jogador escolheu o número: {userNumber}')
    if sum % 2 == 0 and choice == 1 or sum % 2 != 0 and choice == 2:
        count += 1
        print(f'Você venceu!!!!')
    else:
        print(f'Você perdeu! Ao todo, conseguiu ganhar {count} vezes seguidas. Fim de jogo!!')
        break
