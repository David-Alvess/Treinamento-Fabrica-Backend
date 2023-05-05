distanciaEmKm = float(input("Qual a distancia da sua viagem em KM? "))

if distanciaEmKm <= 200.0:
    valor1 = distanciaEmKm * 1.50
    print("O valor da sua passagem é: %.2f !" % valor1)
else:
    valor2 = distanciaEmKm * 1.25
    print("O valor da sua passagem é: %.2f!" % valor2)