palavra = str(input('Digite uma frase: ')).split()
palavra = ''.join(palavra)
palavraInversa = palavra[::-1]
count = 0
for x in range(0, len(palavra)):
    if palavra[x] != palavraInversa[x]:
        print('Não é palídromo')
        break
    else:
        print('É palídromo')
        break