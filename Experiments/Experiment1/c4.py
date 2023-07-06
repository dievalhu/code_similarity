#Deber 1 
#Janmpierre
#Molina

vector=[1605, 3313, 1643, 27064, 1580, 6973]
vector=[23,14,9,6,100,12,18]

#B >= tamano del vector
b=10
hashTable = [[],] * b
contador=0
h_i=0
veces=0
k=0
def tabla_hash(vector,contador,h_i,veces,k):
    posicion= vector[contador] % len(hashTable)

    if hashTable[posicion]!=[] :       
        if veces==0:
            k=(vector[contador] % (len(hashTable)-1))+1
            h_i=(posicion+k) % len(hashTable) 
        if hashTable[h_i]!=[]:
            veces=1
            h_i=(h_i+k) % len(hashTable)
            if h_i==(len(hashTable)-1):
                h_i=0
            tabla_hash(vector,contador,h_i,veces,k)
            
        else:
           
           hashTable[h_i]=vector[contador]
           contador=contador+1
           if contador!=len(vector): 
               tabla_hash(vector,contador,0,0,0) 
               
    else:    
        hashTable[posicion]=vector[contador]
        contador =contador+1
        if contador!=len(vector): 
            tabla_hash(vector,contador,h_i,veces,k) 
    
tabla_hash(vector,contador,h_i,veces,k)

print(hashTable)


