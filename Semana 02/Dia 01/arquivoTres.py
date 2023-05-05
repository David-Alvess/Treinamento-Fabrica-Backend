import random

print('''
1 - Pedra
2 - Papel
3 - Tesoura
4 - Sair
''')

opcaoUsuario = int(input("Digite uma opção de 1 a 3: "))

while (opcaoUsuario < 4):
    opcaoMaquina = random.randint(1,4)
    if opcaoUsuario == opcaoMaquina:
        if opcaoUsuario == 1:
            print("Empate!!! Os dois colocaram Pedra!")
        if opcaoUsuario == 2:
            print("Empate!!! Os dois colocaram Papel!")
        if opcaoUsuario == 3:
            print("Empate!!! Os dois colocaram Tesoura!")

    elif opcaoUsuario == 1:
        if opcaoMaquina == 2: print("Vitoria da maquina! Você colocou Pedra e a maquina Papel!")
        else: print("Você venceu! Você colocou Pedra e a maquina Tesoura")
    elif opcaoUsuario == 2:
        if opcaoMaquina == 1: print("Você venceu! Você colocou Papel e a maquina Pedra!")
        else: print("Vitoria da maquina! Você colocou Papel e a maquina Tesoura!")
    elif opcaoUsuario == 3:
        if opcaoMaquina == 1: print("Vitoria da maquina! Você colocou Tesoura e a maquina Pedra!")
        else: print("Você venceu! Você colocou Tesoura e a maquina Pedra!")
    else: 
        print("Digite uma opção de 1 a 3!")

    opcaoUsuario = int(input("Digite uma opção de 1 a 3: "))