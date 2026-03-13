import random

tentativas = 3
# num = 5
num = random.randint(1,10)

for i in range(tentativas):
    print(f"Tentativa: {i+1}")
    numero = int(input("Digite um numero entre 1 e 10: "))
    while numero > 10 or numero < 1:
        numero = int(input("Digite um numero entre 1 e 10: "))

    if numero == num:
        print("Parabens! Voce acertou o numero")
        break
    else:
        tentativas -= 1
        print("Puxa, nao é esse o numero, continue tentando")

if tentativas == 0:
    print("Puxa, voce nao conseguiu adivinhar o numero")

