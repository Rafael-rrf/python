termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ntermo = 1
while ntermo < 11:
    if ntermo == 1:
        print(f'{ntermo}º termo = {termo}')
        ntermo += 1
    else:
        termo = termo + razao
        print(f'{ntermo}º termo = {termo}')
        ntermo += 1
