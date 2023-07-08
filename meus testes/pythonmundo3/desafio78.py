lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}° valor: ')))
print(lista)

print(f'O primeiro maior número da lista está na posição {lista.index(max(lista))+1} e é {max(lista)}.')
print(f'O primeiro menor número da lista está na posição {lista.index(min(lista))+1} e é {min(lista)}.')
for c in range(0, 5):
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'O maior valor digitado foi {maior} nas posições, ', end='')           
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições, ', end='') 
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}... ', end=" ")
