valores = [23,14,9,6,100,12,18]

print('\t\t\tvalores INGRESADOS\n',valores)

tamano= 10 #n 
hash = ['vacio'] * tamano
for i in range(len(valores)):
  hash_1=valores[i] % tamano
  hash_2=valores[i] % tamano
  if hash[hash_1]=='vacio':
    hash[hash_1]=valores[i]
  else:
    while hash[hash_2]!='vacio':
        k=(valores[i]%(tamano-1))+1
        hash_2 =(hash_2+k)%tamano

  hash[hash_2]=valores[i]
         
print('\t\t\tTABLA HASH\n',hash)