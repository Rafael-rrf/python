n1 = int(input('Digite o tamanho da reta 1: '))
n2 = int(input('Digite o tamanho da reta 2: '))
n3 = int(input('Digite o tamanhp da reta 3: '))
soma = n1 + n2 + n3
maior = 0
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
       maior = n3
if maior < soma - maior:
    print('É possivel criar um triângulo')
else:
    print('Não é possivel criar um triângulo')
