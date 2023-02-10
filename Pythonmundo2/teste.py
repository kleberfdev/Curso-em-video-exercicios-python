lista = [10, 4, 1, 15, 6, 3]
for i in range(0, 5):
    menor = i
    for j in range(i+1, 6):
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
print(lista)
