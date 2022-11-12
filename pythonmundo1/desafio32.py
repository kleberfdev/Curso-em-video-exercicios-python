from datetime import date
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é um ano Bissexto')
else:
    print(f'O Ano {ano} não é um ano Bissexto')
