preco = float(input('Preço das compras: R$ '))
print(''' Formas de pagamento:
[1] dinheiro/cheque
[2] Vencimento
[3] 2X no cartão
[4] 3X ou mais''')

opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 0.1)
elif opção ==2:
    total = preco - (preco * 0.2)
elif opção == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2X de R${parcela:.2f}.')
elif opção == 4:
    total = preco + (preco * 0.2)
    totparcela = int(input('Qual a quantidade de parcelas?: '))
    parcela = total / totparcela
    print(f'Sua compra será parcelada em {totparcela}X de R${parcela:.2f}.')
else:
    print('Essa opção não está disponivel. Escolha uma das opções')
if opção > 0 and opção < 5:
    print(f'Sua compra de R${preco} vai custar R${total} no final')



