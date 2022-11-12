frase = input('Digite a frase: ').upper().strip().rstrip()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(frase.find("A")+1)
print(frase.rfind("A")+1)
