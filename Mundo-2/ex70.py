total = qtdePrecoAcima1000 = barato = 0
nomeBarato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    total += preco
    if barato == 0:
        barato = preco
        nomeBarato = nome
    elif preco < barato:
        barato = preco
        nomeBarato = nome
    if preco > 1000:
        qtdePrecoAcima1000 += 1
    resp = str(input('Deseja continuar? [S] / [N]')).upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida!! Deseja continuar? [S] / [N]')).upper()
    if resp == 'N':
        break
print(f'O preço total foi de: R$ {total}')
print(f'Existe(m) {qtdePrecoAcima1000} produto(s) acima de R$ 1.000,00')
print(f'O nome do produto mais barato é {nomeBarato}')
