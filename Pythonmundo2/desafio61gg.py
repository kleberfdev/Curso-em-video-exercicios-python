pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
termo = pt #primeiro termo vira termo
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo = termo + rz
    cont = cont + 1