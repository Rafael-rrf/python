import datetime
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - anoNasc
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
