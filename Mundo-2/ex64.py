count = 0
soma = 0
resp = 0
while resp != 999:
    resp = int(input('Digite um número [999 p/ sair] :'))
    if resp == 999:
        break
    count += 1
    soma += resp
print(f'Foram computados {count} números e a soma foi {soma}')