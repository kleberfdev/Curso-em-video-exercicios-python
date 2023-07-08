nomes = ('caderno', 'folha', 'lapis', 'mesa')
vogais = ('a', 'e', 'i', 'o', 'u')
for nome in nomes:
    print(f"Na palavra {nome} temos as vogais", end=" ")
    for letra in nome:
        if letra in vogais:
            print(letra, end=" ")
    print()
    

