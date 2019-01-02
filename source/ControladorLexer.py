from source import nxxLexer as lexer
from source.SimbolosNxx import *

global f
f = open('nxx1.txt', "r")
textoFuente = f.read()
print("Here are the tokens returned by the lexer:")

# create an instance of a lexer
lexer.inicializar(textoFuente)

# ------------------------------------------------------------------
# use the lexer.getlist() method repeatedly to get the tokens in
# the sourceText. Then print the tokens.
# ------------------------------------------------------------------
while True:
    token = lexer.get()
    print(token.show(True))
    if token.tipo == FIN_DE_ARCHIVO:
        break
f.close()
