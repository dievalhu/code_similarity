"""
    UNIVERSIDAD POLITECNICA SALESIANA
        APRENDIZAJE DE MAQUINA
    INTEGRANTES:
    -Catucuago Alfredo
    -Chiguano Stalin
    -Dominguez Daniel
    -Estacio Joel
    Implementacion de una hashtable en python
"""
# Importamos liberias


def hashCalculate(num, B):
    hash = num % B
    return hash


def checkHash(hash, hashLog):
    flag = True
    if hash in hashLog:
        return flag
    else:
        flag = False
        return flag


def kCalculate(x, B):
    k = (x % (B - 1)) + 1
    return k


def redispersionHash(k, oldHash, B):
    newHash = (oldHash + k) % B
    return newHash


def run():
    # Introducimos el subconjunto de elementos del ejemplo,datos quemados
    listS = [23, 14, 9, 6, 30, 12, 18]
    # Creamos una variable que tenga el tamaño del subconjunto
    #B = len(listS)
    B = 15
    # vector vacio que llenaremos con los hash
    hashTable = [0 for x in range(0, B)]
    hashLog = ["null" for x in range(0, B)]

    for i in range(0, len(listS)):
        h = hashCalculate(listS[i], B)
        if checkHash(h, hashLog):
            k = kCalculate(listS[i], B)
            r = redispersionHash(k, h, B)

            if checkHash(r, hashLog):
                r2 = redispersionHash(k, r, B)
                hashLog[i] = r2
                hashTable[r2] = listS[i]

            else:
                hashLog[i] = r
                hashTable[r] = listS[i]

        else:
            hashLog[i] = h
            hashTable[h] = listS[i]

    print("La tabla hash es: ")
    print(hashTable)


if __name__ == "__main__":
    run()