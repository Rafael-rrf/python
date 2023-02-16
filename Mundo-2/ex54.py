from datetime import date
maior = 0
menor = 0
for x in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {x}º pessoa: '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo, existem {maior} pessoa(s) de mair e {menor} pessoa(s) de menor ')
