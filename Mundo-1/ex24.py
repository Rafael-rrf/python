cidade = str(input('Digite o nome da sua cidade: ')).upper()
listaPalavras = cidade.split()
resp = 'SANTO' in listaPalavras[0]
print(f'Tem santo no primeiro nome? {resp}')

