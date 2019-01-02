FINDEARCHIVO = b'\0'

# ---------------------------------------------------------------------
#
#                      Carácter
#
# ---------------------------------------------------------------------


class Caracter:
    """
    Un objeto Caracter contiene:
        -Un carácter (self.caracter)
        -El índice de la posición del caráter en el texto fuente
        -El índice de la linea en que el carácter fue encontrado en el texto fuente.
        -El índice de la columna en la linea en que el carácter fue encontrado en el texto fuente.
        -Una referencia al texto fuente (self.textoFuente), de donde se leyó el caracter.


        Esta información estará disponible para el token que contenga este carácter.
        Si un error ocurre, el token puede usar esta información
        para reportar el número de la linea y columna en la que ocurre el error, y mostrar la linea
        en el error ocurrió,
    """

    def __init__(self, c, indiceLinea, indiceCol, indiceTexto, textoFuente):
        """"
        Constructor de la clase Caracter
        """
        self.caracter = c
        self.indiceLinea = indiceLinea
        self.indiceCol = indiceCol
        self.indiceTexto = indiceTexto
        self.textoFuente = textoFuente

    def __str__(self):
        """
        En python el método __str__() retorna una representación de tipo String
        de un objeto. En Java seería equivalente al método toString().
        """

        caracter = self.caracter
        if caracter == " "                 : caracter = "    espacio"
        elif caracter == "\n"              : caracter = "    nueva linea"
        elif caracter == "\t"              : caracter = "    tab"
        elif caracter == FINDEARCHIVO      : caracter = "    eof"

        return(
            str(self.indiceLinea).rjust(6)
           +str(self.indiceCol).rjust(4)
           + "   "
           +str(caracter)
        )


