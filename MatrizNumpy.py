from MatrizBase import *

class MatrizNumpy(MatrizBase):
    def __init__(self, lista:list):
        super().__init__(np.array(lista))

    def determinante(self):
        '''
        Método que devuleve el float de la determinante de la matriz
        Params:
        Returns:
        det = float
        '''
        det = np.around( np.linalg.det(self.get()) , decimals=2)
        return det
    
    def inversa(self):
        '''
        Método que devuleve el object matriz que es la inversa de la matriz
        Params:
        Returns:
        inversa = object
        '''
        if np.linalg.det(self.get()) != 0:
            inversa = MatrizNumpy(np.around(np.linalg.inv(self.get()) , decimals = 2))
        else:
            return 'La Determinante de la matriz es 0, por tanto, no existe su inverso'
        return inversa

    def transpuesta(self):
        '''
        Método que devuleve el object matriz que es la transpuesta de la matriz
        Params:
        Returns:
        transpuesta = object
        '''
        transpuesta = MatrizNumpy(np.transpose(self.get()))
        return transpuesta