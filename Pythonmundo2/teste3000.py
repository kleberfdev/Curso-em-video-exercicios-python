a = 4
b = 10
dia = 0
while a <= b:
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    dia += 1
print(a)
print(b)
print(f'A colônia levou {dia} dias para Igualar ou Ultrapassar.')