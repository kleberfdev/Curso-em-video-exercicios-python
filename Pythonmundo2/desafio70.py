class Car():
    def _init_(self):
        pass

    def imprimirAtributosCarro(self):
        self.modelo = input('Digite o modelo do seu carro: ')
        self.marca = input('Digite a marca do seu carro: ')
        self.preco = input('Digite o preço do seu carro: ')
        self.cor = input('Digite a cor do seu carro: ')
        print(
            f'Bem vindo(a)!\nO modelo do seu carro é {self.modelo}, da marca {self.marca}\nNa cor {self.cor}, ele se encontra na faixa de preço de R${self.preco},00')

    def atendimentoCarro(self):
        self.nomeCliente = input('Digite seu nome: ')
        self.pergunta = input(f'Olá, {self.nomeCliente}! Em quê posso ajudá-lo?\nDigite 1 para a troca de óleo\nDigite 2 para reabastecer\nDigite 3 para verificação rotineira\n')
        if(self.pergunta == '1'):
            valorOleo = float(50.50)
            print(f'Para trocar o óleo, fica no valor de R${valorOleo}')
        elif(self.pergunta == '2'):
            gasolina = float(5.50)
            diesel = float(6.10)
            self.abastecimento = input('Digite 1 para gasolina, ou digite 2 para Diesel ')
            if(self.abastecimento == '1'):
                self.litrosGasolina = input('Quantos litros você quer? ')
                self.precoDoAbastecimentoComGasolina = gasolina * float(self.litrosGasolina)
                print(f'Encher o motor com a gasolina vai custar {self.precoDoAbastecimento}')
            else:
                self.litrosDiesel = input('Quantos litros você quer? ')
                self.precoDoAbastecimentoComDiesel = diesel * float(self.litrosDiesel)
                print(f'Encher o motor com diesel vai te custar {self.precoDoAbastecimentoComDiesel}')
        elif(self.pergunta == '3'):
            valorVerificacao = float(80.90)
            print(f'Para verificar, vai custar {valorVerificacao}')
        else:
            print('Desculpe, não foi uma opção válida. Peço que tente novamente.')
            
hilux = Car()
hilux.imprimirAtributosCarro()
hilux.atendimentoCarro()