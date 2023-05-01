numero1 = int (input("Informe o primeiro numero: "))
numero2 = int (input("Informe o segundo numero: "))
numero3 = int (input("Informe o terceiro numero: "))

if numero1 == numero2 or numero1 == numero3:
    if numero2 == numero3:
        print("Tres numeros iguais")
    else:
        print("Dois numeros iguais")
elif numero2 == numero3:
    print("Dois numeros são iguais")
else:
    print("Tres numeros são diferentes")