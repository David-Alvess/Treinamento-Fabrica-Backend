from random import randint

print('''
    Você irá jogar par ou ímpar! O jogo só será interrompido quando 
    você PERDER, mostrando o total de vitórias consecutivas que você
                conquistou no final do jogo
''')

opcaoUsuario = input("Você quer ser par ou impar? (P/I): ").upper()

qtdeVitoriasUsuario = 0

while True:
    numeroMaquina = randint(0, 99)
    numeroUsuario = int(input("Digite o numero: "))
    soma = numeroMaquina + numeroUsuario

    if opcaoUsuario == 'P':
        if soma % 2 == 0:
            print("Põe essa vitoria pra conta!! Seu numero foi {} e o numero da maquina {}" .format(numeroUsuario, numeroMaquina))
            qtdeVitoriasUsuario += 1
        else:
            print("Essa a maquina venceu :(! Seu numero foi {} e o numero da maquina {}" .format(numeroUsuario, numeroMaquina))
            break
    elif opcaoUsuario == 'I':
        if soma % 2 != 0:
            print("Põe essa vitoria pra conta!! Seu numero foi {} e o numero da maquina {}".format(numeroUsuario, numeroMaquina))
            qtdeVitoriasUsuario += 1
        else:
            print("Essa a maquina venceu :(! Seu numero foi {} e o numero da maquina {}".format(numeroUsuario, numeroMaquina))
            break
    else:
        print("Opção invalida!")
        break

print("Jogo encerrado e você teve uma sequência de {} vitorias!" .format(qtdeVitoriasUsuario))