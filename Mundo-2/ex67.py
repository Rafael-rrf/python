while True:
    resp = int(input('Digite um número que deseja saber a tabuada: '))
    if resp < 0:
        break
    for x in range(1, 11):
        print(f'{x} X {resp} =  {x * resp}')
