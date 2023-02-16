num = int(input('Digite um número: '))
opcao = int(input('Digite 1 para binário, 2 para octal, 3 para hexadecimal: '))

if opcao == 1:
    print(f'A conversão de {num} para binário é de: {bin(num)}')
elif opcao == 2:
    print(f'A conversão de {num} para octal é de: {oct(num)}')
else:
    print(f'A conversão de {num} para hexadecimal é de: {hex(num)}')
