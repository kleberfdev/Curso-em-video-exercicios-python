lista =[]
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    perg = input('Deseja continuar? S/N: ').upper()
    if perg not in 'S':
        break
            



print(f'A lista contém os números {lista}')
print(f'A lista contém os números pares {listapar}')
print(f'A lista contém os números impares {listaimpar}')
