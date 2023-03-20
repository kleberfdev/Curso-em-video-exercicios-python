num = int(input("Digite um número: "))
fib = [0, 1]

while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print("O número está presente na sequência de Fibonacci.")
else:
    print("O número não está presente na sequência de Fibonacci.")
