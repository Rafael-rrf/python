import datetime
anoNasci = int(input('Digite o seu ano de nascimento: '))
anoAtual = datetime.date.today().year

if anoAtual - 18 > anoNasci:
    print(f'Já passou da idade de alistamento!!')
elif anoAtual - 18 == anoNasci:
    print(f'É ano de se alistar')
else:
    print(f'Ainda vai se alistar no serviço militar')