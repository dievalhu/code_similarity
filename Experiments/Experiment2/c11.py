# -*- coding: utf-8 -*-
"""
Deber 1
Grupo 1: Vallejo, Cherrez, Guerra, Cedeño, Contreras

"""

class HashTable:
    def __init__(self, capacity): #Constructor de la clase HashTable
        if capacity < 1:
            raise ValueError("Capacidad debe ser un número entero positivo")
        self.values = capacity * [None] # Definición de la capacidad del HashTable
        
    def __len__(self): 
        return len(self.values)

    def len(self):  #Función que devuelve la longitud del HashTable
        return len(self.values)

    def insert(self, key, value): #Función para la inserción
        index = key % len(self) #Obtención de la posición h(x) = x MOD B
        if self.getIndex(index) is None: #Validación si está vacío se guarda con el índice 
          self.values[index] = value
        else:
          while self.getIndex(index) is not None:  #While que sale cuando en la posición esté vacía o None
            k = (key % (len(self)-1))+1  #k(x) = (x MOD (B-1)) + 1
            index = (index + k ) % len(self) #h_i(x) = (h_i-1(x) + k(x)) MOD B
          self.values[index] = value

    def getIndex(self, index): #Función que devuelve el valor de acuerdo a la posición o índice
        value = self.values[index]
        return value

    def display_hash(self): #Función que muestra la tabla Hash
        for i in range(self.len()):
          print(f'{i} : {self.values[i]}')

tabla1 = HashTable(capacity=10)

tabla1.insert(23,'23')
tabla1.insert(14,'14')
tabla1.insert(9,'9')
tabla1.insert(6,'6')
tabla1.insert(100,'100')
tabla1.insert(12,'12')
tabla1.insert(18,'18')

tabla1.display_hash()