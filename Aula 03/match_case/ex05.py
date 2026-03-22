nota  = float(input("Digite sua nota para verificar a aprovação: "))

match nota:
    case n if n >= 9 :
        print("Nota Excelente")
    case n if n >= 7:
        print("Nota Boa")
    case n if n >= 5:
        print("Nota Regular")
    case _ :
        print("Reprovado")