print('CAIXA ELETRONICO +  ')
saque = int(input('VALOR DO SAQUE : '))
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0
while True:
  if saque >= 50:
    saque = saque - 50
    cedulas50 = cedulas50 + 1
  elif saque >= 20:
    saque =  saque - 20
    cedulas20 = cedulas20 + 1
  elif saque >= 10:
    saque =  saque - 10
    cedulas10 = cedulas10 + 1
  elif saque >= 1:
    saque = saque - 1
    cedulas1 = cedulas1 + 1
  else:
    break
if cedulas50 > 0:
    print(f"Total {cedulas50} de 50 Reais")
if cedulas20 > 0:
    print(f"Total {cedulas20} de 20 Reais")
if cedulas10 > 0:
    print(f"Total {cedulas10} de 10 Reais")
if cedulas1 > 0:
    print(f"Total {cedulas1} de 1 Real")
