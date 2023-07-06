def hash_Function(dividendo, divisor):
    return dividendo % divisor
def k_Value(x, B):
    return hash_Function(x, B - 1) + 1
def rehashing_Function(hPos, k, B):
    return hash_Function(hPos + k, B)
def print_HashTable(hashTable):
    for i in range(len(hashTable)):
        print(i, ' | ', hashTable[i])
def charge_Factor(nElementos, tamTablaHash):
    return nElementos / tamTablaHash
def print_chargeFactor(hashTable):
    nNone = 0;
    for i in range(len(hashTable)):
        if (hashTable[i] is None):
            nNone += 1
    nElementosRegis = len(hashTable) - nNone
    print('Factor de Carga Real: ', charge_Factor(nElementosRegis, len(hashTable)), ' \nElementos:', nElementosRegis,
          '\tCubetas:', len(hashTable))
def is_Prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
def tam_TablaHash_X_ChargeFactor(elementos, factorCargaIdeal):
    tamTablaHash = int(round(len(elementos) / factorCargaIdeal, 0))
    while is_Prime(tamTablaHash) == 0: #B debe ser primo
        tamTablaHash += 1
    else:
        return tamTablaHash
def create_HashTable(elements, len_HashTable):
    hashTable = [None] * len_HashTable
    pos_element = 0;     numCollisions = 0;     pos_hashFlag = False;
    if (len(elements) <= len_HashTable):
        while pos_element < len(elements):
            if pos_hashFlag == 0:
                position = hash_Function(elements[pos_element], len_HashTable)

            if (hashTable[position] is None):
                hashTable[position] = elements[pos_element]
                pos_hashFlag = False
                pos_element += 1
            else:
                numCollisions += 1
                pos_hashFlag = True
                k = k_Value(elements[pos_element], len_HashTable)
                position = rehashing_Function(position, k, len_HashTable)
        print('\nNúmero de colisiones: ', numCollisions)
        print_chargeFactor(hashTable)
        print_HashTable(hashTable)
    else:
        print('No existen suficientes cubetas para el número total de elementos')

elements1 = [23, 14, 9, 6, 30, 12, 18]  # tamaño tabla hash 7
elements2 = [51, 14, 3, 7, 18, 30]  # tamaño tabla hash 11
elements3 = [0, 61, 72, 83, 24, 574, 1000, 9999, 8547899]  # prueba
create_HashTable(elements1, 7)
create_HashTable(elements2, 11)
tamTablaHash = tam_TablaHash_X_ChargeFactor(elements3, 0.75)
create_HashTable(elements3, tamTablaHash)


