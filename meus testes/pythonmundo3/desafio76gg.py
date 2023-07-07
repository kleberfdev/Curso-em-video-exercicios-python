tupla = ('Pão', 3.00, 'Carne', 25.00, 'Frango', 15.00, 'Salmão', 135.00)
print(f'{"-"*40}')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(f'{"-"*40}')
for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<30}R${float(tupla[i+1]):>8.2f}')
print(f'{"_"*40}')

    