def calcula_parcela(valor_emprestimo, num_parcelas, taxa_juros, valor_parcela_inicial):
    remaining_debt = valor_emprestimo
    for i in range(num_parcelas):
        interest = remaining_debt * (taxa_juros / 100)
        if i == 0:
            installment = valor_parcela_inicial + interest
        else:
            installment = interest + remaining_debt / (num_parcelas - i)
        remaining_debt -= installment
        print(f'Parcela {i+1} é de R${installment:.2f}')

valor_emprestimo = 3000
num_parcelas = 4
taxa_juros = 20
valor_parcela_inicial = 750
calcula_parcela(valor_emprestimo, num_parcelas, taxa_juros, valor_parcela_inicial)
