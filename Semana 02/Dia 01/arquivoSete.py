sexo = str(input("Informe o sexo (M/F): "))

while sexo.upper() != "M" and sexo.upper() != "F":
    sexo = str(input("Informe o sexo (M/F): "))

print("Sexo '{}' foi inserido com sucesso! " .format(sexo.upper()))