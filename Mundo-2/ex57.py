s = ''
while s == 'Q':
    s = str(input('Digite seu sexo [M] [F]: ')).upper()
    while s not in 'MF':
        s = str(input('Você digitou uma opção inválida, digite [M] ou [F]: ')).upper()
print('FIM')