n = int(input('Digite um número para calcular seu fatorial: '))
print(f'calculando {n}! = ', end='')
for f in range(n, 0, -1):
    print(f, end='')
    print(' X ' if f > 1 else ' = ', end='')
    n = f * n
print(n)