resp = 'S'
maior = menor = soma = count = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if maior == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja continuar adicionando valores? [S] [N]')).upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida, digite apenas  [S] [N]')).upper()
print(f'soma: {soma}')
print(f'media: {soma/count}')
print(f'Foram registrados {count} números')
print(f'maior: {maior}')
print(f'menor {menor}')

