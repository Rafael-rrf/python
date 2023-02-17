n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número número: '))
resp = 99
while resp != 5:
    print('*=' * 30)
    resp = int(input('O que deseja fazer com os números?\n 1 - Somar\n 2 - Multiplicar\n 3 - Maior\n 4- novos números\n 5 - Sair do programa\n'))
    print('*=' * 30)
    if resp == 1:
        print(f'A soma de {n1} + {n2} é: {n1+n2}')
    elif resp == 2:
        print(f'A multiplicação de {n1} x {n2} é: {n1 * n2}')
    elif resp == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        elif n1 < n2:
            print(f'O maior é o {n2}')
        else:
            print(f'Os números são iguais')
    elif resp == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número número: '))
    else:
        if resp != 5 or type(resp) != int:
            resp = int(input('Opção inválida!!! Digite uma opção válida: '))
        else:
            break
print('Fim')
