
aluno = {}
nome = input('Informe o nome do aluno: ')
media = float(input('Informe a media do aluno: '))

aluno['Nome'] = nome
aluno['Média'] = media

print('Dados do aluno: ')

for chave, valor in aluno.items():
    print(chave + ' : ', valor)