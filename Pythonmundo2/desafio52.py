num = int(input('Digite um número e veja se ele é primo: '))
mult = 0
print('Os múltiplos são: ', end="")
for c in range(1, num + 1):
    if num % c == 0:
        mult = mult + 1
        print(c, end=" ")
print(f'\nTem {mult} múltiplos')
if mult == 2:
    print('É primo')
else:
    print('Não é primo')