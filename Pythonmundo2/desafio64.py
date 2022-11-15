num = c = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma = soma + num
        c = c + 1
print(f'Você digitou {c} números e a soma deles é de {soma}')    
