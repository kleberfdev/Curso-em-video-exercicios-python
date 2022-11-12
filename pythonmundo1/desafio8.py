#Converter metros em cm
from lib2to3.pytree import convert


n = float(input('Quantos metros? '))

c = n * 100
m = n * 1000

print('A quantidades de centimetros em {} metros é {}'.format(n, c))
