vel = int(input('Qual a Velocidade do Carro? '))
difvel = vel - 80
multa = difvel * 7
if vel > 80:
    print('Você excedeu a velocidade em {} e sua multa vai ser de {}'.format(difvel, multa))
else:
    exit()