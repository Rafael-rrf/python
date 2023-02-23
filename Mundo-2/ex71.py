count50 = count20 = count10 = count1 = 0
while True:
    saque = int(input('Digite o valor a ser sacado: '))
    count50 = saque // 50
    if count50 > 0:
        print(f' {count50} cédulas de R$ 50,00')
    saque = saque - (count50 * 50)
    count20 = saque // 20
    if count20 > 0:
        print(f' {count20} cédulas de R$ 20,00')
    saque = saque - (count20 * 20)
    count10 = saque // 10
    if count10 > 0:
        print(f' {count10} cédulas de R$ 10,00')
    saque = saque - (count10 * 10)
    count1 = saque
    if count1 > 0:
        print(f' {count1} cédulas de R$ 1,00')
