numero = int(input("Informe o numero para consulta da tabuada: "))

while numero >= 0:

    for i in range (1, 10):
        tabuada = numero * i
        print("{} x {} = {}" .format(numero , i, tabuada))

    numero = int(input("Informe um novo valor para consulta da tabuada ou um numero negativo para sair: "))

print("Programa encerrado!")