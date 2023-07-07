c = 0
valores = pares = ()
while True:
    if c < 4:
        valor = int(input(f'Digite o {c + 1}° valor: '))
        valores = valores + (valor, )
        if valor % 2 == 0:
            pares = pares + (valor, ) 
        c += 1
    else:
        break
print(f'A tupla com os 4 valores é {valores}')
print(f'O 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição {valores.index(3)+1}.')
else:
    print('O Valor 3 não foi digitado.')
if () in pares:
    print(f'Os números pares são: {pares}.')
else:
    print('Não contém números.')