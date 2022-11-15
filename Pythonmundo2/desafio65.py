opção = 'S'
c = 0
num = num1 = maior = menor = media = 0
while opção in 'S':
        c = c + 1
        num = int(input(f'Digite o {c} número: '))
        print('Quer informar mais números? [S/N]')
        opção = str(input('Qual a sua a opção? ').upper())
        while opção not in 'SN':
            print('Escolha uma dessas opções: [S/N]')
            opção = str(input('Qual a sua a opção? ').upper())
  
        num1 = num1 + num
        media = num1 / c
        if c == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num



    

print(f'A média dos valores dos {c} incluídos é de {media}')
print(f'O maior número entre eles é {maior}')
print(f'O menor número entre eles é {menor}')

