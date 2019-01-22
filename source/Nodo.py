from .Token import Token


"""Clase Nodo para el Arbol Abstracto Sintáctico - AST"""

class Nodo:
    def __init__(self, token=None):
        self.token = token
        self.nivel = 0
        self.children = [] #lista de nodos hijo

    def agregar(self, token):
        """
        Crea un nodo a partir de un token y lo agrega a self.children
        """
        self.agregarNodo(Nodo(token))

    def agregarNodo(self, nodo):
        """
        agrega un nodo a la lista de hijos
        """
        nodo.nivel = self.nivel+1
        self.children.append(nodo)

    def toString(self):
        s = "     " * self.nivel
        if self.token == None
            s += "RAÍZ\n"
        else:
            s += self.token.caracter + "\n"

        for child in self.children:x
            s += child.toString()
        return s
