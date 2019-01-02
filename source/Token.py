from source import Escaner


# class LexerError(Exception):
#     print('Fin de archivo encontrado inesperadamente')
#
# class LexerStangeCharacterFound(Exception):
#     print('Encontré algo que no reconozco')

# ----------------------------------------------------------
#       Token
# ----------------------------------------------------------

class Token:
    """
    Un objeto Token es el tipo de objeto que un lexer retorna
    contiene:
    -El texto del token ( 1 o más caracteres)
    -El tipo de token que es
    -El número de linea y columna en la que el token comienza
    """

    def __init__(self, caractInicial):
        """
        Constructor de la clase Token
        """
        self.caracter = caractInicial.caracter

        # -------------------------------------------------
        # El Token recoleta información
        #  sobre su posición en el texto fuente
        # -------------------------------------------------

        self.textoFuente = caractInicial.textoFuente
        self.indiceLinea = caractInicial.indiceLinea
        self.indiceCol   = caractInicial.indiceCol

        # -----------------------------------------------------
        # No sabemos que tipo de token va a ser hasta que
        # hayamos terminado de procesar todos los caracteres
        # que harán parte del token
        # por lo que inicialmente el tipo del token sera nulo.
        # ------------------------------------------------------

        self.tipo = None

    # ----------------------------------------------------------
    # retorna una representación del token en formato String
    #------------------------------------------------------------
    def show(self, mostrarNumerodeLinea=False, **kwargs):
        """
        align=True shows token type left justified with dot leaders.
        Specify align=False to turn this feature OFF.
        """
        align = kwargs.get("align", True)
        if align:
            tokenTypeLen = 12
            space = " "
        else:
            tokenTypeLen = 0
            space = ""

        if mostrarNumerodeLinea:
            s = str(self.indiceLinea).rjust(6) + str(self.indiceCol).rjust(4) + "  "
        else:
            s = ""
        if self.tipo == self.caracter:
            s = s + "Símbolo".ljust(tokenTypeLen, ".") + ":" + space + self.tipo
        elif self.tipo == "Espacio en blanco":
            s = s + "Espacio en blanco".ljust(tokenTypeLen, ".") + ":" + space + repr(self.caracter)
        else:
            s = s + self.tipo.ljust(tokenTypeLen, ".") + ":" + space + self.caracter
        return s

    guts = property(show)


