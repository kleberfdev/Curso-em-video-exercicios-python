frase = str(input('Digite a frase: ')).strip().upper().replace(' ', '')
inverso = ''
for letra in range(len(frase)-1, -1, -1 ):#pegando da última letra para a primeira
    inverso = inverso + frase[letra]
if inverso == frase:
    print(f'A frase {frase} invertida é {inverso}, nisso ela é um palídromo')
else:
    print(f'A frase {frase} invertida é {inverso}, nisso ela não é um palidromo')