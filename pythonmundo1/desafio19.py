import random
alu1 = str(input('Digite o nome do aluno 1: '))
alu2 = str(input('Digite o nome do aluno 2: '))
alu3 = str(input('Digite o nome do aluno 3: '))
alu4 = str(input('Digite o nome do aluno 4: '))

lista = [alu1, alu2, alu3, alu4]
resul = random.choice(lista)

print('O sorteado foi {}'.format(resul))
