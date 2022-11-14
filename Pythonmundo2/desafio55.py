lista = []
for c in range(1, 6):
    peso = float(input(f'Digite o {c}° peso '))
    lista.append(peso)
print(f'O maior peso é {max(lista)}')
print(f'O menor peso é {min(lista)}')