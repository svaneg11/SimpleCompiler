from source.nxxLexer import Lexer
from source.SimbolosNxx import *
from source.Token import LexerError
from source.Token import LexerStrangeCharacterFound

global f
f = open('nxx1.txt', "r")
textoFuente = f.read()
print("\nEstos son los tokens retornados por el lexer:")

# create an instance of a lexer
lexer = Lexer(textoFuente)

# ------------------------------------------------------------------
# use the lexer.getlist() method repeatedly to get the tokens in
# the sourceText. Then print the tokens.
# ------------------------------------------------------------------

while True:
    try:
        token = lexer.get()
        print(token.show(True))
        if token.tipo == FIN_DE_ARCHIVO:
            break
    except LexerError:
        print('Error: fin de archivo encontrado inesperadamente')
    except LexerStrangeCharacterFound:
        print('Error: carácter irreconocible encontrado')
f.close()
