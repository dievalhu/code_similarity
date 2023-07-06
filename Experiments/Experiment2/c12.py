"""
Deber 1
Grupo 2: Morales, Montalvo
"""

class HashTable:
    def __init__(self, capacidad): 
        if capacidad < 1:
            raise ValueError("Capacidad debe ser un número entero positivo")
        self.values = capacidad * [None] # def de capacidad 
        
    def __len__(self): 
        return len(self.values)

    def len(self):  #longitud de tabla 
        return len(self.values)

    def insertar(self, jey, value): #fun de insercion
        indice = jey % len(self) #Obtención de la posición h(x) = x MOD B
        if self.getindice(indice) is None: #Validación si está vacío se guarda con el índice 
          self.values[indice] = value
        else:
          while self.getindice(indice) is not None:  #While que sale cuando en la posición esté vacía o None
            j = (jey % (len(self)-1))+1  #j(x) = (x MOD (B-1)) + 1
            indice = (indice + j ) % len(self) #h_i(x) = (h_i-1(x) + j(x)) MOD B
          self.values[indice] = value

    def getindice(self, indice): #Función que devuelve el valor de acuerdo a la posición o índice
        value = self.values[indice]
        return value

    def mostrar_hash(self): #Función que muestra la tabla Hash
        for i in range(self.len()):
          print(f'{i} : {self.values[i]}')

tabla2 = HashTable(capacidad=10)

tabla2.insertar(23,'23')
tabla2.insertar(14,'14')
tabla2.insertar(9,'9')
tabla2.insertar(6,'6')
tabla2.insertar(100,'100')
tabla2.insertar(12,'12')
tabla2.insertar(18,'18')

tabla2.mostrar_hash()