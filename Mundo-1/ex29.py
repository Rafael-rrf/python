speed = int(input('Velocidade: '))

if speed > 80:
    print(f'Você foi multado em R$ {(speed-80) * 7},00')