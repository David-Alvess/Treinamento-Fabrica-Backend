numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundoo numero: "))
numero3 = float(input("Digite o terceiro numero: "))
numero4 = float(input("Digite o quarto numero: "))
numero5 = float(input("Digite o quinto numero: "))

def maiorNumero(a, b, c, d, e):
    max = a

    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    if e > max:
        max = e

    return max

print("{:.2f} é o maior numero " .format(maiorNumero(numero1, numero2, numero3, numero4, numero5)))