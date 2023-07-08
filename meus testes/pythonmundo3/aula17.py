lanche = ['pizza', 'refrigerante', 'hotdog']
valores = list(range(4,11))
valores1 = [1, 5, 3, 9, 7]
if 'pizza' in lanche:
    lanche.remove('pizza')
    print(lanche)
lanche.insert(0, 'pizza')
lanche.append('sanduiche')
print(lanche)
print(valores)
valores1.sort()
print(valores1)
valores.sort(reverse=True)
print(valores)