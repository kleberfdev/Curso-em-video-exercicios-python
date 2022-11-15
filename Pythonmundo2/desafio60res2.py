n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1 #fator de soma = 0 / fator multip = 1
print(f'calculando {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c -1
print(f)