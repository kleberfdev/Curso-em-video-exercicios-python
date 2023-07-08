valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for v in valores:
    print(v, end=" ")
print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim')