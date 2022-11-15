opção = 'S'
c = num = soma = media = 0
while opção in 'S':
        c = c + 1
        num = int(input(f'Digite o {c} número: '))
        print('Quer informar mais números? [S/N]')
        opção = str(input('Qual a sua a opção? ').upper())
        while opção not in 'SN':
            print('Escolha uma dessas opções: [S/N]')
            opção = str(input('Qual a sua a opção? ').upper())  
        soma = soma + num
        media = soma / c
        if c == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
print(f'A média dos valores dos {c} incluídos é de {media}')
print(f'O maior número entre eles é {maior}')
print(f'O menor número entre eles é {menor}')

