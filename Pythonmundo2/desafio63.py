qtd = int(input('Digite a quantidade de elementos: '))
c = 1
num1 = 0
num2 = 1
print(num1)
print(num2)
cont = 3
while c <= qtd:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    c = c + 1
    print(num3)