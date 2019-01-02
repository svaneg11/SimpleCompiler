import string
"""
Especificación de los símbolos pertenecientes al lenguaje 'nxx'
"""

FINDEARCHIVO = b'\0'

# -------------------------------------------------
#       Palabras clave (keywords)
# -------------------------------------------------
keywords = """
if
then
else
elif
endif
while
loop
endloop
print
return
exit
"""
keywords = keywords.split()

# -------------------------------------------------
#       Símbolos de 1 carácter de longitud
# -------------------------------------------------
simbolosUnCaracter = """
=
( )
< >
/ * - +
! &
. ;
"""
simbolosUnCaracter = simbolosUnCaracter.split()

# -------------------------------------------------
#       Símbolos de 2 caracteres de longitud
# -------------------------------------------------
simbolosDosCaracteres = """
==
<=
>=
<>
!=
++
**
--
+=
-=
||
"""
simbolosDosCaracteres = simbolosDosCaracteres.split()


# ----------------------------------------------------------
#       Espacios en blanco, letras, números
#       y símbolos validos para nombrar variables, etc
# ----------------------------------------------------------
IDENTIFICADOR_CARACTERES_INICIALES = string.ascii_letters
IDENTIFICADOR_CARACTERES = string.ascii_letters + string.digits + "_"

NUMERO_CARACTERES_INICIALES = string.digits
NUMERO_CARACTERES = string.digits + "."

STRING_CARACTERES_INICIALES = "'" + '"'
ESPACIOS_EN_BLANCO_CARACTERES = " \t\n"


# ---------------------------------------------------
#       Tipos de Token para cosas que no son
#       símbolos o palabras clave
# ---------------------------------------------------
STRING = "String"
IDENTIFICADOR = "Identificador"
NUMERO = "Number"
ESPACIO_EN_BLANCO = "Espacio en blanco"
COMENTARIO = "Comentario"
FIN_DE_ARCHIVO = "eof"