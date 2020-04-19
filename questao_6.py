#duas tuplas de números inteiros, uma com os ímpares e outra com os pares

def obter_listas(tupla):
    impares = []
    pares = []

    for i in range (len(tupla)):
        if tupla[i] %2 !=0:
            impares.append(tupla[i])

        if i % 2 == 0:
            pares.append(tupla[i])

    return impares, pares
print(obter_listas((3,14,15,92,65,359)))