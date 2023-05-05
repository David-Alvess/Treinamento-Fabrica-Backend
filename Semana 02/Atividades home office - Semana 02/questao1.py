from datetime import datetime, timedelta

dataNascimento = int(input('Informe seu ano de nascimento: '))
dataAtual = datetime.now().year

idade = dataAtual - dataNascimento

if idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    print("Você tem mais de 18 anos. Já se passou {} ano(s) do tempo de se alistar!" .format(idade - 18))
else:
    print("Ainda não é a hora de se alistar e falta(m) {} ano(s) para você se alistar!" .format(18 - idade))
