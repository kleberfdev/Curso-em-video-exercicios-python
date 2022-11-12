# Achar a raiz quadrada
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
#Com duas casas decimais
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Achar a raiz quadrada arredondada
print('A raiz de {} arredondada para cima é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é igual a {}'.format(num, math.floor(raiz)))