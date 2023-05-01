frase = (input("Digite a frase:"))
contador_de_letras = 0;

for letra in frase:
    if letra.isalpha():
        contador_de_letras += 1;

print("Esta frase possui {} letras" .format(contador_de_letras))