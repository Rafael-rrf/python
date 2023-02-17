n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior!!')
else:
    if n2 > n1 and n2 > n3:
        print(f'{n2} é o maior!!')
    else:
        print(f'{n3} é o maior!!!')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor!!')
else:
    if n2 < n1 and n2 < n3:
        print(f'{n2} é o menor!!')
    else:
        print(f'{n3} é o menor!!!')
