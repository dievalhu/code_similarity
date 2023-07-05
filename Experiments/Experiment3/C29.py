#Universidad Politecnica Salesiana
#Ingenieria en Ciencias de la Computacion
#Machine Learning
#Deber #1
#Integrantes: Chacon Bryan - Morales Paul - Robles Michael - Romero Jefferson - Ruano Boris - Valencia Leyton
B= 11
nums = [23,14,9,6,30,12,18]  
nuevo = ['Na' for x in range(B)]
for n in nums:
    if nuevo[n%B] == 'Na':
        nuevo[n%B] = n
    else: 
        h0=n%B
        k=n%(B-1)+1
        h1=(h0+k)%B
        if nuevo[h1] != 'Na':
            h1=(h1+k)%B
        nuevo[h1]=n
print(nuevo)



