frase = input("Digite a frase: ")
palavra = input("Digite a palavra para busca: ")

busca_palavra = bool(frase.upper().count(palavra.upper()))

print(busca_palavra)