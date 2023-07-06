def hash_funcion(dividendo, divisor):
    return dividendo % divisor
def k_valor(x, B):
    return hash_funcion(x, B - 1) + 1
def rehashing_Funcion(hPos, k, B):
    return hash_funcion(hPos + k, B)
def print_hashTablee(hashTablee):
    for i in range(len(hashTablee)):
        print(i, ' | ', hashTablee[i])
def charge_Factor(nElementos, tamanoTablaHash):
    return nElementos / tamanoTablaHash
def print_chargeFactor(hashTablee):
    nNinguno = 0;
    for i in range(len(hashTablee)):
        if (hashTablee[i] is None):
            nNinguno += 1
    nElementosRegs = len(hashTablee) - nNinguno
    print('Factor de Carga Real: ', charge_Factor(nElementosRegs, len(hashTablee)), ' \nElementos:', nElementosRegs,
          '\tCubetas:', len(hashTablee))
def is_Prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
def tam_TablaHash_X_ChargeFactor(elementos, factorCargaIdeal):
    tamanoTablaHash = int(round(len(elementos) / factorCargaIdeal, 0))
    while is_Prime(tamanoTablaHash) == 0: #B debe ser primo
        tamanoTablaHash += 1
    else:
        return tamanoTablaHash
def create_hashTablee(elements, len_hashTablee):
    hashTablee = [None] * len_hashTablee
    pos_elemento = 0;     numCollisions = 0;     pos_hashFlag = False;
    if (len(elements) <= len_hashTablee):
        while pos_elemento < len(elements):
            if pos_hashFlag == 0:
                posicion = hash_funcion(elements[pos_elemento], len_hashTablee)

            if (hashTablee[posicion] is None):
                hashTablee[posicion] = elements[pos_elemento]
                pos_hashFlag = False
                pos_elemento += 1
            else:
                numCollisions += 1
                pos_hashFlag = True
                k = k_valor(elements[pos_elemento], len_hashTablee)
                posicion = rehashing_Funcion(posicion, k, len_hashTablee)
        print('\nNúmero de colisiones: ', numCollisions)
        print_chargeFactor(hashTablee)
        print_hashTablee(hashTablee)
    else:
        print('No existen suficientes cubetas para el número total de elementos')

elementos1 = [23, 14, 9, 6, 30, 12, 18]  # tamaño tabla hash 7
elementos2 = [51, 14, 3, 7, 18, 30]  # tamaño tabla hash 11
elements3 = [0, 61, 72, 83, 24, 574, 1000, 9999, 8547899]  # prueba
create_hashTablee(elementos1, 7)
create_hashTablee(elementos2, 11)
tamanoTablaHash = tam_TablaHash_X_ChargeFactor(elements3, 0.75)
create_hashTablee(elements3, tamanoTablaHash)


