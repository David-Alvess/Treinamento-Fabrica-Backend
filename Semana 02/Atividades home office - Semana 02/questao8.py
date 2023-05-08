
numero = int(input(("Informe o primeiro numero: ")))
lista_de_numeros = []
lista_de_numeros.append(numero)

opcaoSair = (input("Deseja inserir um novo valor? (S/N): "))

while opcaoSair.upper() == 'S':
    outrosNumeros = int(input(("Informe o proximo numero: ")))
    lista_de_numeros.append(outrosNumeros)
    opcaoSair = (input("Deseja inserir um novo valor? (S/N): "))

menorNumero = min(lista_de_numeros)
maiorNumero = max(lista_de_numeros)
media = sum(lista_de_numeros) / len(lista_de_numeros)

print("O menor numero é: {}" .format(menorNumero))
print("O maior numero é: {}" .format(maiorNumero))
print("A media é: {}" .format(media))