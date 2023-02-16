maior = menor = 0
for x in range(1, 6):
    n = int(input(f'Digite o peso da {x}ª Pessoa: '))
    if x == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'A pessoa mais pesada tem {maior} quilos e a mais leve tem {menor} quilos')
