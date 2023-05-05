frase = str(input("Digite a frase: "))
contaString = len(frase) - frase.count(" ")

print("Na frase {} contém {} letras" .format(frase, contaString))