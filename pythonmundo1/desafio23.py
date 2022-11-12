num = int(input('Digite o número: '))


print(f'unidade: {num % 10}')
print(f'dezena: {num // 10 % 10}')
print(f'centena: {num // 100 % 10}')
print(f'milhar: {num // 1000 % 10}')
