total = totmil = cont = menor = 0
prodbarato = " "
while True:
    produto = str(input("Qual o Nome do Produto? "))
    preço = float(input("Qual o Preço? R$ "))
    cont += 1        
    total += preço
    if cont == 1 or preço < menor:
        menor = preço
    if preço > 1000:
        totmil +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'O total de itens acima de 1000 Reais é {total:.2f}')
print(f'O Produto com menor preço é {prodbarato} com valor de {menor:.2f}')