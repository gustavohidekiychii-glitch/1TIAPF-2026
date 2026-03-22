matriz = [
    [1,2],
    [3,4]
]

escalar = int(input("Digite o numero escalar para multiplicar a matriz: "))

for i in range(2):
    for j in range(2):
        matriz[i][j] *= escalar

for linha in matriz:
    print(linha)