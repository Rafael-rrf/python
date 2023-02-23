maior18 = qtdeHomem = mulherMenor20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M] ou [F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido!! Digite o sexo [M] ou [F] ')).upper()
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        qtdeHomem += 1
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1
    resp = str(input('Deseja continuar? [S/N]')).upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida! Digite [S] ou [N] !!'))
    if resp == 'N':
        break
print(f'Foram cadastradas {maior18} pessoas maiores de idade')
print(f' Foram cadastradas {mulherMenor20} mulher(es) menores que 20 anos')
print(f' Foram cadastrados {qtdeHomem} homens')