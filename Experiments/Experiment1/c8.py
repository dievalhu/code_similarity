datos = [23,14,9,6,100,12,18]

print('\t\t\tDATOS INGRESADOS\n',datos)

tamaño= 10 #n 
hash = ['vacio'] * tamaño
for i in range(len(datos)):
  hash1=datos[i] % tamaño
  hash2=datos[i] % tamaño
  if hash[hash1]=='vacio':
    hash[hash1]=datos[i]
  else:
    while hash[hash2]!='vacio':
        k=(datos[i]%(tamaño-1))+1
        hash2 =(hash2+k)%tamaño

  hash[hash2]=datos[i]
         
print('\t\t\tTABLA HASH\n',hash)