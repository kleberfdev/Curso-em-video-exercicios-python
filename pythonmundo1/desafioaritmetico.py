#Ler antecessor e sucesso de número inteiro
n = int(input('Digite o número '))
a = n - 1
s = n + 1
d = n * 2
t = n * 3
r = n ** (1/2)




print('O antecessor e sucessor do número {} são respctivamente {} e {}; e seu dobro {}, \
seu triplo {} e a raiz quadrada é {:.0f}.'.format(n, a ,s, d, t, r))

