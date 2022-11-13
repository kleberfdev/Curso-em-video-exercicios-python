frase = str(input('Digite a frase: ')).strip().upper().replace(' ', '')
inverso = frase[::-1]
if inverso == frase:
    print(f'A frase {frase} invertida é {inverso}, nisso ela é um palídromo')
else:
    print(f'A frase {frase} invertida é {inverso}, nisso ela não é um palidromo')
    #1 onde a frase começa literalmente não importa se está ao contrário
#2 onde a frase termina - 0 é o inicio ou fim e sem valor pega a frase toda
#3  1 diz da esquerda para direita e -1 o inverso