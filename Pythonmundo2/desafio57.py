sexo = str(input('Digite o sexo: [M/F]')).upper()
while sexo not in 'MF':
    sexo = str(input('Informe seu sexo conforme ao lado: [M/F]')).upper()
print('Sexo confirmado')
