num = int(input("Digite um numero par: "))

while num % 2 != 0:
    num = int(input("Digite novamente um numero par: "))

print(f"O numero par digitado foi: {num}")