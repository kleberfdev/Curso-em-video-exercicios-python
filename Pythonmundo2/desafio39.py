from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print(idade)

if idade == 17:
    print('É o seu ano de alistamento')
elif idade > 17:
    if idade - 17 == 1:
        print(f'Você deve se alistar, pois está atrasado {idade - 17} ano')
    else:
        print(f'Você deve se alistar, pois está atrasado {idade - 17} anos')
elif idade < 17:
    if (idade - 17) * -1 == 1:
        print(f'Calma, que ainda não é o tempo de se alistar falta {(idade - 17) * -1} ano')
    else:
        print(f'Calma, que ainda não é o tempo de se alistar faltam {(idade - 17) * -1} anos')