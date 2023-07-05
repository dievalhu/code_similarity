#Integrantes
#Cordova-Idrovo-Morales J-Morocho-Rios-Salgado

#crea el vector de posiciones con NA
def creacionVectorB(B):
  tabla=['NA']
  tabla*=B
  return tabla

#asigna posicion a cada elemento
def asignarPos(vector, B):
  lv=list()
  if(len(vector)>B):
    print('B es menor que el numero de elementos')
  else:
    lv = creacionVectorB(B)

    #recorre cada elemnto del vector
    for i in range(len(vector)):
      #calculo h(x)
      hx = vector[i]%B
      #asigna posicion si no esta lleno
      if(lv[hx]=='NA'):
        lv[hx]=vector[i]
      else:
        #calculo k(x) = (x MOD (B-1)) + 1
        kx = (vector[i] % (B-1)) + 1
        bandera = True
        #asigno hxi
        while(bandera):
          #calculo de hxi
          hxn = (hx+kx)%B
          if(lv[hxn]=='NA'):
            #si hxi encuentra vacio el espacio se guarda
            lv[hxn]=vector[i]
            bandera=False
          else:
            #el nuevo hx es hxn, para siguiente iteracion
            hx = hxn

  return lv

#se crea el vector y B
#v = [23,14, 9, 6, 30, 12, 18]
#B = 7

v = [23,14,9,6,30,12,18]  
B = 11
#se corre la funcion y se imprime
lv = asignarPos(v,B)
print(lv)