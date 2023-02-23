termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtdeTermo = int(input('Digite quantos termos deseja: '))
termoAtual = 1
while termoAtual < qtdeTermo + 1:
    if termoAtual == 1:
        print(f'{termoAtual}º termo = {termo}')
        termoAtual += 1
    else:
        termo = termo + razao
        print(f'{termoAtual}º termo = {termo}')
        termoAtual += 1