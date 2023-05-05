import random

numeroMaquina =  random.randint(0, 10)
numeroUsuario = int(input("Informe um numero: " ))
i = 0

while numeroMaquina != numeroUsuario:
    numeroUsuario = int(input("Erroooooou! Informe outro numero: " ))
    i += 1

print("Você acertou e usou um total de {} tentativas" .format(i))
