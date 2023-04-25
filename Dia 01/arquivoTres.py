import random
aluno1 = str(input("Digite o primeiro nome: "))
aluno2 = str(input("Digite o segundo nome: "))
aluno3 = str(input("Digite o terceiro nome: "))

listAluno = [aluno1, aluno2, aluno3]

print ("O nome sorteado foi: " + listAluno [random.randrange(len(listAluno))])