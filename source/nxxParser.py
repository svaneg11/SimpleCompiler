from .nxxLexer import Lexer
from .SimbolosNxx import *
from .Nodo import Nodo

class ParserError(Exception):
    pass


def dq(s):
    return '"%s"' %s

token = None
verbose = False
indent = 0
numberOperator = ["+", "-", "*", "/"]
lexer = Lexer()
# -----------------------------------
#
# -----------------------------------
def getToken():
    global token
    if verbose:
        if token:
            # print the current token, before we get the next one
            # print (" "*40) + token.show()
            print("  "*indent + "   (" + token.show(align=False) + ")")
    token = lexer.get()

#------------------------------------
# push and pop
#------------------------------------
def push(s):
    global indent
    indent += 1
    if verbose:
        print(("  " * indent) + " " + s)

def pop(s):
    global indent
    if verbose:
        # print(("  "*indent) + " " + s + ".end")
        pass
    indent -= 1
