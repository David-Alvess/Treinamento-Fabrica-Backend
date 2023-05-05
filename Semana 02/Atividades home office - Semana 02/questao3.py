from datetime import datetime

anoNascimento = int (input('Informe seu ano de nascimento: '))
anoAtual = datetime.now().year

idade = int (anoAtual - anoNascimento)

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')