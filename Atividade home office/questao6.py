data_nascimento = int(input("Informe o seu ano de nascimento: "))
ano_atual = 2023

idade = ano_atual - data_nascimento

if idade >= 18:
    print("Você é maior de idade! Sua idade é {} anos" .format(idade))
else:
    print("Você é menor de idade! Sua idade é {} anos" .format(idade))