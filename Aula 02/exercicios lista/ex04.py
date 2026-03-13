nomes = ["rafael","leo","caique","luany","caio"]

index = nomes.count(input("Digite um nome a ser procurado na lista: "))

if index > 0:
    print("Nome na lista")
else:
    print("Nome nao esta na lista")

nomeBusca = input("Digite um nome a ser procurado na lista: ")
if nomeBusca in nomes:
    print("Nome na lista")
else:
    print("Nome nao esta na lista")