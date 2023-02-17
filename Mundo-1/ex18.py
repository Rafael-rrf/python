import math

a = int(input('Digite um ângulo: '))
rad = math.radians(a)
print(f'Seu seno é: {math.sin(rad)}\n Seu cosseno é: {math.cos(rad)}\n Tangente: {round(math.tan(rad))}')
