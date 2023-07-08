#Ainda está ligado com a
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(a)
print(b)
#Cópia não está mais ligado
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)