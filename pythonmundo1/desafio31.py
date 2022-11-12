dist = int(input('Qual a distancia em Km? '))
vgpq = dist * 0.5
vggd = dist * 0.45
if dist <= 200:
    print('O preço da viagem é {}'.format(vgpq))
else:
    print('O preço da viagem é {}'.format(vggd))