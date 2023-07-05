#!/usr/bin/env python
# coding: utf-8
# ESTRATEGIA DE REDISPERSIÓN CON 2ª FUNCION HASH:

# Integrantes:
# Lomas Alvaro
# Mariño Daniel
# Raza Sebastian
# Romo Joel
# Sarmiento Steven
# Pillajo Jhony
# In[1]:


B = 11                          #Tamaño Tabla HASH
lv = ['none'] * B              #Tabla HASH con todos sus elementos 'none'
v = [23,14,9,6,30,12,18]       #Elementos a insertar
for x in v:
    pos = x%B                  #MOD (Función HASH)
    while lv[pos] != 'none':   #Mientras la posición no tenga un elemento 'none' realiza Redispersión
        k = (x%(B-1))+1
        pos = (pos+k)%B 
    else:                      #Al encontrar 'none' en una posición, ubica el elemento 
        lv[pos] = x
print(lv)                      #Imprime la tabla en forma de vector
for x in range(0, B):     
    print(x,'-->',lv[x])       #Imprime la tabla con posiciones
# In[ ]:




