#Deber 1 
#Janmpierre
#Molina

vect=[1605, 3313, 1643, 27064, 1580, 6973]
vect=[23,14,9,6,100,12,18]

#B >= tamano del vect
b=10
hashTabla = [[],] * b
cont=0
h_j=0
n_veces=0
k=0
def hash_tabla(vect,cont,h_j,n_veces,k):
    n_posicion= vect[cont] % len(hashTabla)

    if hashTabla[n_posicion]!=[] :       
        if n_veces==0:
            k=(vect[cont] % (len(hashTabla)-1))+1
            h_j=(n_posicion+k) % len(hashTabla) 
        if hashTabla[h_j]!=[]:
            n_veces=1
            h_j=(h_j+k) % len(hashTabla)
            if h_j==(len(hashTabla)-1):
                h_j=0
            hash_tabla(vect,cont,h_j,n_veces,k)
            
        else:
           
           hashTabla[h_j]=vect[cont]
           cont=cont+1
           if cont!=len(vect): 
               hash_tabla(vect,cont,0,0,0) 
               
    else:    
        hashTabla[n_posicion]=vect[cont]
        cont =cont+1
        if cont!=len(vect): 
            hash_tabla(vect,cont,h_j,n_veces,k) 
    
hash_tabla(vect,cont,h_j,n_veces,k)

print(hashTabla)


