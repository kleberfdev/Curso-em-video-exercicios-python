#Dissecando uma Variável

a = input('Digite Algo ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print ('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())