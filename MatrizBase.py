def _menor(lista):
        min = lista[0];
        for x in lista:
            if x < min:
                min = x
        return min
import numpy as np

class MatrizBase:
    def __init__(self, matriz):
        self.__matriznativa = matriz
        self.__shape = []
        self.setdi()
    
    def get(self):
        '''
        Método que devuelve el atributo self.__matriznativa
        Params:
        Returns:
        self.__matriznativa
        '''
        return self.__matriznativa

    def setdi(self):
        '''
        Método que devuelve una lista con (renglon, columna)
        '''
        sub1 = len(self.__matriznativa)
        self.__shape.append(sub1)
        sub2 = len(list(self.__matriznativa[0]))
        self.__shape.append(sub2)
        return self.__shape

    def prod_escalar(self, escalar:int):
        '''
        Método que devuleve el object matriz que es la matriz multiplicada por un escalar, elemento a elemento
        Params:
        escalar = int
        Returns:
        matriz_escalar = object
        '''
        matriz_escalar = MatrizBase([[self.get()[i][j] * escalar for j in range(len(self.get()[0]))] for i in range(len(self.get()))])
        return matriz_escalar
    
    def suma(self, otra:object):
        '''
        Método que devuleve el object matriz que es la suma de las matrices
        Params:
        otra = object
        Returns:
        matriz_suma = object
        '''
        if len(self.__matriznativa) != len(otra.__matriznativa) or len(self.__matriznativa[0]) != len(otra.__matriznativa[0]): #en la segunda condicion es [0] pues da igual que fila me tome para verificar
            return 'Dimensiones no congruentes'
        else:
            for i in range(len(self.__matriznativa)):
                for j in range(len(self.__matriznativa[i])):
                    self.__matriznativa[i][j] += otra.__matriznativa[i][j]
        matriz_suma = MatrizBase(self.__matriznativa)     
        return matriz_suma

    def minimo(self):
        '''
        Método que devuleve el int minimo de la matriz
        Params:
        Returns:
        minimo = int
        '''
        minimo =_menor(list(self.__matriznativa[0]))
        for lista in self.__matriznativa:
            if minimo > _menor(lista):
                minimo = _menor(lista)
        return minimo

    
    def __str__(self): #namas pa probar lo que hagamos
        matriz_str = ""
        for i in range(len(self.__matriznativa)):
            for j in range(len(self.__matriznativa[i])):
                matriz_str += str(self.__matriznativa[i][j]) + " "
            matriz_str += "\n"
        return matriz_str
