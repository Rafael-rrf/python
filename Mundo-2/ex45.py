from random import randrange
opcoes = ['Pedra', 'Papel', 'Tesoura']
opcaoMaquina = opcoes[randrange(0, 3)]
numero = int(input("""Escolha uma opção:
  0 -Papel
  1 - Pedra
  2 - Tesoura\n"""))
opcaoPlayer = opcoes[numero]

if opcaoPlayer == opcaoMaquina:
    print(f' A Máquina escolheu {opcaoMaquina} e o jogador escolheu {opcaoPlayer}, DEU EMPATE!!!')
elif opcaoPlayer == 'Papel' and opcaoMaquina == 'Pedra' or opcaoPlayer == 'Pedra' and opcaoMaquina == 'Tesoura' or opcaoPlayer == 'Tesoura' and opcaoMaquina == 'Papel':
    print(f' A Máquina escolheu {opcaoMaquina} e o jogador escolheu {opcaoPlayer}, O PLAYER GANHOU!!!')
else:
    print(f' A Máquina escolheu {opcaoMaquina} e o jogador escolheu {opcaoPlayer}, A MÁQUINA GANHOU!!!')