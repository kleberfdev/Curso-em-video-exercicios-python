nd = soma = 0
while True:
    num = int(input('Digite o número: '))
    if num == 999:
        break
    nd = nd + 1
    soma = soma + num
print(f'Foram digitados {nd} números, sendo sua soma de {soma}')