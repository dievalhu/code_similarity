# -*- coding: utf-8 -*-
"""Untitled45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUzuScDba1BLeKdvN8FRwtmjF_EE21tM
"""

#integrantes: Andres Ponce, Ketherine Ramirez, Dylan Lopez
tam = 11
vec= [23,14,9,6,30,12,18]  
if tam == "": B = len(vec)
else: B = int(tam)
th = ['nada' for i in range(B)]
def funcionx(x):
    return x % B

def funcionK(x):
    return x % (B-1) + 1

def funcionH(h1, k):
    return (h1+k) % B

def insertarTH(pos,dato):
    if th[pos] == 'nada':
        del th[pos]
        th.insert(pos,dato)
        return True
    else:
        return False

for i in range(len(vec)):
    valor = vec[i]
    H0 = funcionx(valor)
    estado = insertarTH(H0, valor)
    print(th)
    while not estado:
        K = funcionK(valor)
        H0 = funcionH(H0, K)
        estado = insertarTH(H0, valor)

print("Tabla Hash: {}".format(th))