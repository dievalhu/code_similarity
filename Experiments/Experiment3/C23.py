
n = 7 #tamano de la lista
hash = [None] * n
datos = [23,14,9,6,30,12,18]
ndatos = len(datos)
print(hash)
#h(23)= 23 mod 7 => 2
for i in range(ndatos):
  h=datos[i] % n
  h0=datos[i] % n
  if hash[h]==None:
    hash[h]=datos[i]
  else:
    while hash[h0]!=None:
        k=(datos[i]%(n-1))+1
        h0 =(h0+k)%n

  hash[h0]=datos[i]
         
print("Tabla Hash:")
print(hash)