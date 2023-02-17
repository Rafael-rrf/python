dist = int(input('Digite a distancia em KM: '))

if dist <= 200:
    print(f'O valor a ser pago é: R${0.5 *dist:.2f}')
else:
    print(f'O valor a ser pago é: R${0.45 * dist:.2f}')