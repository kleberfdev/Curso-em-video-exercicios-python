print('=' * 40)
print('Bem vindo a simulação de sua casa nova: ')
print('=' * 40)
vcasa = float(input('Qual o valor da casa? '))
print('=' * 40)
salario = float(input('Qual o seu salário? '))
print('=' * 40)
anos = int(input('Em quantos anos deseja pagar '))
print('=' * 40)
meses = anos * 12

if (vcasa / meses) <= (salario * 0.30):
    print('Parabéns o valor foi aprovado')
else:
    print('Infelizmente o valor não foi aprovado ')
    print(f'Para pagar uma casa de {vcasa} em {anos}, a prestação será de {(vcasa / meses):.2f}')