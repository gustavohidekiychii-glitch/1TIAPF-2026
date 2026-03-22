print("====== Menu ======")
print(" 1 - Ver perfil")
print(" 2 - Editar perfil")
print(" 3 - Sair")
print()

while True:
    opcao = int(input("Digite um das opções do menu: "))

    match opcao:
        case 1 :
            print("Ver perfil selecionado!")
            break
        case 2 :
            print("Editar perfil selecionado!")
            break
        case 3 :
            print("Saindo...")
            break
        case _ :
            print("Opção invalida, tente novamente!")