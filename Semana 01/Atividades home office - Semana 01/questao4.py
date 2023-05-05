numero = float(input("informe o numero: "))
if numero != 0:
    if numero % 2 == 0:
        print("O numero {} é par!" .format(numero))
    else:
        print("O numero {} é impar!" .format(numero))

else:
    print("Zero é neutro!")