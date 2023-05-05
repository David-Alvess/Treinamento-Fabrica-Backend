frase = input("Digite a frase: ").strip().lower()
frase_sem_Espaco_e_minuscula = frase.replace(" ", "")
frase_invertida = frase_sem_Espaco_e_minuscula[::-1]

print(frase_sem_Espaco_e_minuscula)
print(frase_invertida)

if frase_sem_Espaco_e_minuscula == frase_invertida:
    print("É um palindromo")