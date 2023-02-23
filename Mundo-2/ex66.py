count = sum = 0
while True:
    resp = int(input(f'Digite um número (999 p/ parar): '))
    if resp == 999:
        break
    count += 1
    sum += resp
print(f'A soma foi de {sum} e foram digitados {count} números')
