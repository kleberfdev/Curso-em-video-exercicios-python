from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('Você é da categoria MIRIM')
elif idade <=14 :
    print('Você é da categoria INFANTIL')
elif idade <= 19:
    print('Você é da categoria JUNIOR')
elif idade <= 25:
    print('Você é da categoria SÊNIOR')
else:
    print('Você é da categoria MASTER')
