somaIdade = 0
nomeVelho = ''
idadeMaisVelho = 0
mulheresAbaixo20Anos = 0
for x in range(1, 5):
    print('~'*30)
    print(f'\033[1:32mDados da {x}ª pessoa: \033[m')
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo [M] ou [F] :')).upper()
    idade = int(input('Digite sua idade: '))
    somaIdade += idade
    if sexo == 'M' and idade > idadeMaisVelho:
        nomeVelho = nome
        idadeMaisVelho = idade
    if sexo == 'F' and idade < 20:
        mulheresAbaixo20Anos += 1
print('#-'*30)
print(f'A média de idade é de: {somaIdade/4} anos')
print(f'O nome do homem mais velho é: {nomeVelho}')
print(f'Existe {mulheresAbaixo20Anos} mulheres abaixo de 20 anos.')
print('#-'*30)
