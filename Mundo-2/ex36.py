valor = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário: '))
anos = int(input('Digite a quantidade de anos para pagar: '))
meses = anos * 12
prestacao = valor / meses

if prestacao < salario * 0.3:
    print(f'Crédito Aprovado!!! Você terá que pagar uma parcela de {prestacao} durante {meses} meses')
else:
    print(f'Crédito não aprovado!!! A parcela superou 30% do valor do seu salário')

