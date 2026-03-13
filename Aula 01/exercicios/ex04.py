distancia = float(input("Qual a distancia percorrida em Kms: "))
velMedia = float(input("Qual a velocidade média em Km/H: "))

tempo = distancia / velMedia
horas = int(tempo)
minutos = int((tempo - horas) * 60)

print(f"O tempo estimado de viagem é de {horas}H:{minutos}m")