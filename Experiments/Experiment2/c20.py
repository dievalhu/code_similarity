#Nombres: Juan, Perrez 

list = [23,14,9,6,30,12,18]
def doble_hashing(valores, tamTabla):
    tableHash = [None] * tamTabla #creation table hash
    for i in range(len(valores)):
        hash_1 = valores[i] % tamTabla # 1st hash, form: xMODB
        if tableHash[hash_1] is None:
            tableHash[hash_1] = valores[i] #add value of the list in the hash_1 position
        else:
            hash_2 = hash_1 # change values for hash_2 
            while tableHash[hash_2] is not None:
                k__x = (valores[i]%(tamTabla-1))+1
                hash_2 = (hash_2 + k__x) % tamTabla 
            tableHash[hash_2] = valores[i] #asigna valor de la list en la posicion del hash_2
    return tableHash 
print( doble_hashing(list, 10))
