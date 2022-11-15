pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
termo = pt #primeiro termo vira termo
cont = 1
termocont = 0
ncont = 10
while ncont != 0:
    termocont = termocont + ncont
    while cont <= termocont:
        print(termo, end=' ')
        termo = termo + rz
        cont = cont + 1
    ncont = int(input('\nQuer mais quantos termos: '))
print(f'Progresssão finalizada com {termocont} termo/s mostrado/s')
print('Finalizado')