frase = str(input('Digite uma frase: ')).lower()
print(frase[::-1])
print(f'A letra "A" aparece: {frase.count("a")} vezes')
print(f'Ela aparece primeiro na {frase.find("a")} posição')
print(f'Ela aparece na ultima vem em { len(frase) - frase[::-1].find("a")}')