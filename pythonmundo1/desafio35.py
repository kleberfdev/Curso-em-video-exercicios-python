reta1 = float(input('Digite o Valor da reta 1: '))
reta2 = float(input('Digite o Valor da reta 2: '))
reta3 = float(input('Digite o Valor da reta 3: '))
lista = [reta1, reta2, reta3]
lista.sort()
if (min(lista) + lista[1]) > max(lista):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
