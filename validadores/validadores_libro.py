import re
expresion_titulo = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,60}$"
expresion_paginas = "^[0-9]{1,5}$"


def validar_titulo(titulo):
    validador = re.compile(expresion_titulo)
    return validador.match(titulo)

def validar_paginas(paginas):
    validador = re.compile(expresion_paginas)
    return validador.match(paginas)