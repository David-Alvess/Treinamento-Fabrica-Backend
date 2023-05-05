valorDaCasa = float(input("Informe o valor da casa que deseja comprar: "))
salarioDoComprador = float(input("Informe o salario do comprador: "))
valorMaximoParcela = salarioDoComprador * 0.30
anosParaPagar = int(input("Informe o prazo em anos para pagamento: "))

valorDaPrestacao = valorDaCasa / (anosParaPagar * 12)

if valorDaPrestacao <= valorMaximoParcela:
    print("Financiamento liberado! A prestação será de {:.2f}" .format(valorDaPrestacao))
else:
    print("Financiamento recusado!")
