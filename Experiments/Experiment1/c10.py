#Nombres: Juan, Perrez 

lista = [23,14,9,6,30,12,18]
def double_hashing(valores, tamTabla):
    tablaHash = [None] * tamTabla #creation table hash
    for i in range(len(valores)):
        hash1 = valores[i] % tamTabla # 1st hash, form: xMODB
        if tablaHash[hash1] is None:
            tablaHash[hash1] = valores[i] #add value of the list in the hash1 position
        else:
            hash2 = hash1 # change values for hash2 
            while tablaHash[hash2] is not None:
                k_x = (valores[i]%(tamTabla-1))+1
                hash2 = (hash2 + k_x) % tamTabla 
            tablaHash[hash2] = valores[i] #asigna valor de la list en la posicion del hash2
    return tablaHash 
print( double_hashing(lista, 10))
