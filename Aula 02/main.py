numeros = [1,2,3,4,5]

#comentario
numeros.append(6)
print(numeros)

numeros2 = [7,8,9]
numeros.extend(numeros2) #extend
print(numeros)

numeros.insert(4,10)
print(numeros)

numeros.append(1)
numeros.remove(1)
print(numeros)

removido = numeros.pop(6)
print(f"O numero removido da lista foi o: {removido}")
print(numeros)

print(numeros2)
numeros2.clear()
print(numeros2)

index = numeros.index(6)
print(f"O elemento procurado esta no index: {index}")

numero = 10
vezes = numeros.count(numero)
print(f"O numero {numero} se repete {vezes} vez(es)")

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

novaNumeros = numeros.copy()
numeros.remove(10)
print(novaNumeros)
