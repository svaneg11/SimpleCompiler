from source.nxxLexer import Lexer
from source.SimbolosNxx import *
#from source.Token import LexerError
#from source.Token import LexerStangeCharacterFound


global f
f = open('nxx1.txt', "r")
textoFuente = f.read()
print("Here are the tokens returned by the lexer:")

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
    except Exception:
        print("Error")
        break
f.close()
