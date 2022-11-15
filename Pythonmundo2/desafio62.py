pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
termo = pt #primeiro termo vira termo
cont = 1
ncont = 10
termocont = 0
while cont <= ncont:
    print(termo, end=' ')
    termo = termo + rz
    cont = cont + 1
    termocont = termocont + 1
    if cont == (ncont + 1):
        print('\nVocê quer mostrar mais termos? [S/N]')
        opção = str(input('Digite a opção: ').upper())
        while opção not in 'NS':
            opção = str(input('Digite a opção entre essas [S/N]: ').upper())
        if opção == 'S':
            ncont = int(input('Digite mais quantos termos: '))
            cont = 1
print(f'Progresssão finalizada com {termocont} termo/s mostrado/s')
print('Finalizado')