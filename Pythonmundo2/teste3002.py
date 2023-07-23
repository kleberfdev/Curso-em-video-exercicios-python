emprestimo = float(input('De quanto você precisa emprestado? R$ ' ))
parcelas = int(input('Em quantas parcelas quer dividir? '))

totalemprestimo = emprestimo + (emprestimo * 0.2)

total = totalemprestimo / parcelas

print(f"O valor total acrescido dos juros é de R$ {totalemprestimo:.2f}")
print(f"O valor de cada parcela será R$ {total:.2f}")
