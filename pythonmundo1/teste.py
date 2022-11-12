from random import sample
def embaralha(palavra):
    a = sample(palavra,len(palavra))
    d = ''.join(a)
    print(a)
    print(d.lower())
palavra = input("Digite a Palavra ")
embaralha(palavra)