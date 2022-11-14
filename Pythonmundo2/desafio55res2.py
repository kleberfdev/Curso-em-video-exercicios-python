maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa '))
    if p == 1:
        maior = peso
        print(maior)
        menor = peso
        print(menor)
    else:
        if peso > maior:
            maior = peso
            print(f'novo peso {maior} maior')
        if peso < menor:
            menor = peso
            print(f'novo peso {menor} menor')
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')
