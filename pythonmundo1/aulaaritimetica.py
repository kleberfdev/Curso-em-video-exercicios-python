print(3//3)
print(3**3)
print(2%2)

print('oi' + 'olá')
print('oi' * 5)
print('=' * 20)
print('=' * 20)

nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
print('A soma vale {}'.format(n1+n2))
print('A soma vale {}'.format(s), end=' ')
print('A multiplicação vale {}'.format(m))
print('A soma é {}, a multiplicação é {}, a divisão é {} e a divisão flutuante com até 3 digitos é {:.3f}'.format(s, m, d, d))
