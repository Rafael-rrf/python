def maiorNumero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3
def condTriangulo(n1, n2, n3):
    if maiorNumero(n1, n2, n3) < (n1 + n2 + n3) - maiorNumero(n1, n2, n3):
        print('Pode ser um triângulo')
        if n1 == n2 == n3:
            print('O triângulo é do tipo Equilátero')
        elif n1 != n2 and n1 != n3 and n2 != n3:
            print('O triangulo é do tipo Escaleno')
        else:
            print('O triângulo é do tipo Isosceles')
    else:
        print('Não pode ser um triângulo')

n1 = int(input('Digite a medida do primeiro lado: '))
n2 = int(input('Digite a medida do segundo lado: '))
n3 = int(input('Digite a medida do terceiro lado: '))

condTriangulo(n1, n2, n3)


