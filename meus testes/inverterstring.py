texto = str(input('Digite o texto: '))
lista_caracteres = list(texto)

for i in range(len(lista_caracteres)//2):
    lista_caracteres[i], lista_caracteres[-i-1] = lista_caracteres[-i-1], lista_caracteres[i]

novo_texto = ''.join(lista_caracteres)

print(novo_texto)
