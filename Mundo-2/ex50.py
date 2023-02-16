soma = 0
for x in range(1, 7):
    n = int(input(f'Digite o {x}° número: '))
    if n % 2 == 0:
        soma+= n
print(soma)