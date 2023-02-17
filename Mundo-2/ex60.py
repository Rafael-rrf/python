num = int(input('Digite um número para calcular seu fatorial: '))
valor = num
mult = num
while num != 1:
    mult *= num - 1
    num = num - 1
print(f'O fatorial de {valor} é: {mult}')