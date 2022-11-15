c = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma = soma + num
    c = c + 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma deles é de {soma}')    
