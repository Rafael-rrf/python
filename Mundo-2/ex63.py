num = int(input('Digite a quantidade de números que você quer exibir na sequencia Fibonacci: '))
count = 1
ant = 1
atual = 1
while count < num + 1:
    if count == 1 or count == 2:
        print(f' {count}º número da sequencia: {atual}')
        count += 1
        ant = 1
        atual = 1
    else:
        seq = atual + ant
        print(f'{count}º número da sequencia: {seq}')
        ant = atual
        atual = seq
        count += 1

