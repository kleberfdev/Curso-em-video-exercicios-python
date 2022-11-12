 #calcular valor de um angulo qualquer e mostre o valor do seno, cosseno e tangente
import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo {} tem como seno {:.5f}, cosseno {:.5f} e tangente {:.5f}'.format(ang, sen, cos, tang))
