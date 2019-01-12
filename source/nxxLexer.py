from .Escaner import Escaner
from .Token import *
from .SimbolosNxx import *
from .Caracter import *
import copy


class Lexer:

    def __init__(self, textoFuente):
        self.scanner = Escaner.Escaner(textoFuente)
        self.c1, self.c2 = self.scanner.get()

    def getChar(self):
        self.c1, self.c2 = self.scanner.get()

    def get(self):
        """
        Construye y retorna el siguiente token en el texto fuente
        """

        # --------------------------------------------------------------------------------
        # Lee del texto fuente e ignora los espacios blancos y comentarios -- START
        # --------------------------------------------------------------------------------
        while self.c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES or self.c2.caracter == '/*':
            # procesar espacio en blanco
            while self.c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES:
                token = Token(self.c1)
                token.tipo = ESPACIO_EN_BLANCO
                self.getChar()

                while self.c1.caracter in ESPACIOS_EN_BLANCO_CARACTERES:
                    token.caracter += self.c1.caracter
                    self.getChar()

                # retornar token solo si queremos procesar espacios en blanco

            # procesar comentarios

            while self.c2.caracter == '/*':
                # Encontramos el inicio de un comentario
                token = Token(self.c2)
                token.tipo = COMENTARIO
                token.caracter = self.c2.caracter
                self.getChar()

                while not(self.c2.caracter == '*/'):
                    if self.c1.caracter == FIN_DE_ARCHIVO:
                        pass
                    token.caracter += self.c1. caracter
                    self.getChar()
                token.caracter += self.c1.caracter
            # retornar token solo si se quieren procesar los comentarios

        # --------------------------------------------------------------------------------
        # Lee del texto fuente e ignora los espacios blancos y comentarios -- FIN
        # --------------------------------------------------------------------------------

        # Crear un nuevo token
        # El token toma la información del número de linea y columna del carácter


        token = Token(self.c1)

        if self.c1.caracter == FINDEARCHIVO:
            token.tipo = FIN_DE_ARCHIVO
            return Token

        if self.c1.caracter in IDENTIFICADOR_CARACTERES_INICIALES:
            token.tipo = IDENTIFICADOR
            self.getChar()

            while self.c1.caracter in IDENTIFICADOR_CARACTERES:
                token.caracter += self.c1.caracter
                self.getChar()

            return token

        if self.c1.caracter in NUMERO_CARACTERES_INICIALES:
            token.tipo = NUMERO
            self.getChar()

            while self.c1.caracter in NUMERO_CARACTERES:
                token.caracter += self.c1.caracter
                self.getChar()

            return token

        if self.c1.caracter in STRING_CARACTERES_INICIALES:
            simboloString = self.c1.caracter
            token.tipo = STRING
            self.getChar()

            while not (self.c1.caracter == simboloString):
                if self.c1.caracter == FINDEARCHIVO:
                    raise LexerError
                token.caracter += self.c1.caracter
                self.getChar()

            token.caracter += self.c1.caracter
            return token

        if self.c2.caracter in simbolosDosCaracteres:
            token = Token(self.c2)
            token.caracter = self.c2.caracter

            # Para estos simbolos el tipo es igual a los caracteres del token
            token.tipo = token.caracter
            self.getChar()
            return token

        if self.c1.caracter in simbolosUnCaracter:
            # Para estos simbolos el tipo es igual a los caracteres del token
            token.tipo = token.caracter
            self.getChar()
            return token

        else:
            token.tipo = FIN_DE_ARCHIVO
            return token
