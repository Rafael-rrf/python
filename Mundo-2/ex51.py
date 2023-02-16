termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão'))

print(f'Os 10 primeiros termos da P.A são: ')
for x in range(1, 11):
    if x == 1:
        termoAtual = termo
        print(f'{x}° Termo = {termo}')
    else:
        termoAtual += razao
        print(f'{x}° Termo = {termoAtual}')
