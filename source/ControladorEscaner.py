from source import Escaner as scanner
""""
Este módulo inicializa el escaner, pasandole una cadena de texto para que lea
e imprimiendo cada caracter que obtiene del escaner
"""


print("\nLos siguientes son los carácteres obtenidos por el escaner:\n")
print("  linea col caracter")


# Abrir archivo fuente
file = open('nxx1.txt', 'r')
textoFuente = file.read()

# Inicializar el scanner
scanner.inicializar(textoFuente)

caract = scanner.get()
while(True):
    print("{}".format(caract))
    if caract.caracter == scanner.FINDEARCHIVO:
        break
    caract = scanner.get()
