frase = str("Treinamento hoje de backend")

print("A frase atualmente é: '{}'" .format(frase))

palavra_para_substituir = str(input("Informe a palavra na frase que deseja substituir: "))
nova_palavra = str(input("Informe a paravra que deseja inserir: "))

frase = frase.replace(palavra_para_substituir, nova_palavra)

print("A palavra atualizada é: '{}'" .format(frase))