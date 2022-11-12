#fórmula da hipotenusa = h²=ca²+co²
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hipotenusa = ((ca**2)+(co**2))**(1/2)
print('A hipotenusa é {}'.format(hipotenusa))