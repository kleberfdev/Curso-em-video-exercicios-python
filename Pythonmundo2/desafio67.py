c = 0
while True:
    num = int(input('Digite um número e veja a sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
        c = c + 1
print('Encerrou')