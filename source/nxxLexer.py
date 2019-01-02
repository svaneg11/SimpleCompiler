from source import Escaner as scanner
from .Token import *
from .SimbolosNxx import *
from .Caracter import *
import copy

c1, c2 = 0,0


def inicializar(textoFuente):
    global c1
    global c2

    scanner.inicializar(textoFuente)
    c1 = scanner.get()
    c2 = c1


def getChar():
    global c1, c2
    c2 = copy.copy(c1)
    c1 = scanner.get()
    c2.caracter += c1.caracter


def get():
    """
    Construye y retorna el siguiente token en el texto fuente
    """
    global c1, c2

    # --------------------------------------------------------------------------------
    # Lee del texto fuente e ignora los espacios blancos y comentarios -- START
    # --------------------------------------------------------------------------------
    while c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES or c2.caracter == '/*':
        # procesar espacio en blanco
        while c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES:
            token =  Token(c1)
            token.tipo = ESPACIO_EN_BLANCO
            getChar()

            while c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES:
                token.caracter += c1
                getChar()

            # retornar token solo si queremos procesar espacios en blanco

        # procesar comentarios

        while c2.caracter == '/*':
            # Encontramos el inicio de un comentario
            token = Token(c2)
            token.tipo = COMENTARIO
            token.caracter = c2.caracter
            getChar()

            while not(c2.caracter == '*/'):
                if c1.caracter == FIN_DE_ARCHIVO:
                    pass
                token.caracter += c1.caracter
                getChar()
            token.caracter += c1.caracter
        # retornar token solo si se quieren procesar los comentarios

    # --------------------------------------------------------------------------------
    # Lee del texto fuente e ignora los espacios blancos y comentarios -- FIN
    # --------------------------------------------------------------------------------

    # Crear un nuevo token
    # El token toma la información del número de linea y columna del carácter

    getChar()

    token = Token(c1)

    if c1.caracter == FINDEARCHIVO:
        token.tipo = FIN_DE_ARCHIVO
        return Token

    elif c1.caracter in IDENTIFICADOR_CARACTERES_INICIALES:
        token.tipo = IDENTIFICADOR
        getChar()

        while c1.caracter in IDENTIFICADOR_CARACTERES:
            token.caracter += c1.caracter
            getChar()

        return token

    elif c1.caracter in NUMERO_CARACTERES_INICIALES:
        token.tipo = NUMERO
        getChar()

        while c1.caracter in NUMERO_CARACTERES:
            token.caracter += c1.caracter
            getChar()

        return token

    elif c1.caracter in STRING_CARACTERES_INICIALES:
        simboloString = c1.caracter
        token.tipo = STRING
        getChar()

        while not (c1.caracter == simboloString):
            if c1.caracter == FINDEARCHIVO:
                pass
            token.caracter += c1.caracter
            getChar()

        token.caracter += c1.caracter
        return token

    elif c2.caracter in simbolosDosCaracteres:
        token = Token(c2)
        token.caracter = c2.caracter

        # Para estos simbolos el tipo es igual a los caracteres del token
        token.tipo = token.caracter
        return token

    elif c1.caracter in simbolosUnCaracter:
        # Para estos simbolos el tipo es igual a los caracteres del token
        token.tipo = token.caracter
        return token

    else:
        token.tipo = FIN_DE_ARCHIVO
        return token
