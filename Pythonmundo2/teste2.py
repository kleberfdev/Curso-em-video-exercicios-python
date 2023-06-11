nome = input("Digite o seu nome: ")

lista = [("Kleber", ""), 
         ("Kleber", ""), 
         ("Kleber", "Belo Horizonte")]

for tupla in lista:
    if tupla[0] == nome:
        if tupla[1] == "":
            continue
        else:
            print(f"A cidade de {nome} é {tupla[1]}.")
            break
else:
    print(f"{nome} não foi encontrado na lista.")

