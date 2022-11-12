reta1 = float(input('Digite o valor da primeira reta '))
reta2 = float(input('Digite o valor da segunda reta '))
reta3 = float(input('Digite o valor da terceira reta '))
lista = [reta1, reta2, reta3]
if min(lista) + (lista[1]) > max(lista):
    print('Com as Informações dadas é possivel fazer um triângulo ', end = '')
    if reta1 == reta2 == reta3:
        print('equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('isósceles')
    else: #pode ser colocado r1 != r2 != r3 != r1
        print('escaleno')
else:
    print('Com as Informações dadas não é possivel fazer um triângulo')
