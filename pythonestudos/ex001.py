print('=' * 40)
print('Bem vindo a simulação de sua casa nova: ')
print('=' * 40)

emprestimo = float(input("Qual valor você deseja da casa ? "))

salario_comprador = float(input("Qual o seu salário ? "))

tempo_pag = int(input("Em quantos anos você vai pagar ? "))

meses = tempo_pag * 12

#calculo_salario = print(f"{salario_comprador*30/100}")
calculo_salario = salario_comprador * 0.30

valor_prestacao = emprestimo / meses

if valor_prestacao <= calculo_salario:
  print("Empréstimo aprovado")

else:
  print("Empréstimo reprovado")