nomes = ('caderno', 'folha', 'lapis', 'mesa')
for nome in nomes:
    print(f"\nNa palavra {nome} temos as vogais", end=" ")
    for letra in nome:
        if letra in 'aeiou':
            print(letra, end=" ")

