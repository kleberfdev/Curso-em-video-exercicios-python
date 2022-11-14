'''for c in range(1, ?): #while substitui o inteerrogação que não pode ser incluso no for
    n = int(input('Digite um valor: '))'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('fim')