lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > max(lista):
        lista.append(valor)
        print('Adicionado ao final da lista')
    else:
        for i in range(len(lista)):
            if valor < lista[i]:
                lista.insert(i, valor)
                print("Adicionado na posição", i)
                break
print(lista)