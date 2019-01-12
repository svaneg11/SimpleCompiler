from .Caracter import *
import copy

class Escaner:

    """
    Un objeto escaner lee un texto fuente
    y retorna un caracter a la vez.
    """

    def __init__(self, textoAEscanear):
        self.textoFuente = textoAEscanear
        self.indiceFinal = len(self.textoFuente)-1
        self.indiceTexto = -1
        self.indiceLinea = 0
        self.indiceCol = -1


    def get(self):
        """
        retorna el siguiente carácter en el texto fuente
        """

        self.indiceTexto += 1
        if self.indiceTexto > 0:
            if self.textoFuente[self.indiceTexto-1] == '\n':
                self.indiceLinea += 1
                self.indiceCol = -1
        self.indiceCol += 1

        if self.indiceTexto > self.indiceFinal:
            car = Caracter(FINDEARCHIVO, self.indiceLinea, self.indiceCol, self.indiceTexto, self.textoFuente)
            car2 = copy.copy(car)
        else:
            c = self.textoFuente[self.indiceTexto]
            car = Caracter(c, self.indiceLinea, self.indiceCol, self.indiceTexto, self.textoFuente)
            car2 = copy.copy(car)
            if self.indiceTexto+1 < self.indiceFinal:
                nextCar = self.textoFuente[self.indiceTexto+1]
                car2.caracter += nextCar
            else:
                car2 = copy.copy(car)
        return car, car2
