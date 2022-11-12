nome = input("Digite seu nome: ")

def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
texto = converter_maiuscula(flag_maiuscula=True, texto=nome) # Passagem nominal de parâmetros
print(texto)