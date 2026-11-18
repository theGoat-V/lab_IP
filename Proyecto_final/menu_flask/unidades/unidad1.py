"""Unidad 1: conversión de bases, números primos y Fibonacci."""
from .ayuda import entero, trabajo

MSG = "Escribe un número entero mayor o igual a 0."


def _n(v):
    return entero(v["numero"], minimo=0, msg=MSG)


CAMPO = [{"name": "numero", "label": "Número entero (decimal)", "type": "number", "valor": ""}]


def binario(v):                                        # 01_Binario.py
    Numero = _n(v)
    if Numero == 0:
        return ["0"]
    binario = ""
    while Numero > 0:
        residuo = Numero % 2
        binario = str(residuo) + binario
        Numero = Numero // 2
    return [binario]


def octal(v):                                          # 02_octal.py
    Numero = _n(v)
    if Numero == 0:
        return ["0"]
    octal = ""
    while Numero > 0:
        residuo = Numero % 8
        octal = str(residuo) + octal
        Numero = Numero // 8
    return [octal]


def hexadecimal(v):                                    # 03_Hexadecimal.py
    Numero = _n(v)
    if Numero == 0:
        return ["0"]
    letras = "0123456789ABCDEF"
    hexadecimal = ""
    while Numero > 0:
        residuo = Numero % 16
        hexadecimal = letras[residuo] + hexadecimal
        Numero = Numero // 16
    return [hexadecimal]


def binario_compacto(v):                               # 04_binario_compacto.py
    Numero, binario = _n(v), ""
    if Numero == 0:
        return ["0"]
    while Numero > 0: binario, Numero = str(Numero % 2) + binario, Numero // 2
    return [binario]


def octal_compacto(v):                                 # 05_octal-compactado.py
    Numero, octal = _n(v), ""
    if Numero == 0:
        return ["0"]
    while Numero > 0: octal, Numero = str(Numero % 8) + octal, Numero // 8
    return [octal]


def hexadecimal_compacto(v):                           # 06_Hexal_compacto.py
    Numero, hexadecimal = _n(v), ""
    if Numero == 0:
        return ["0"]
    while Numero > 0: hexadecimal, Numero = "0123456789ABCDEF"[Numero % 16] + hexadecimal, Numero // 16
    return [hexadecimal]


def es_primo(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def primo(v):                                          # 07_primo.py
    return ["primo" if es_primo(_n(v)) else "no primo"]


def primo_fibonacci(v):                                # 08_primofibonacci.py
    numero = _n(v)
    if not es_primo(numero):
        return ["No es primo"]
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return ["Es primo", "Esta en Fibonacci" if a == numero else "No esta en Fibonacci"]


UNIDAD = {
    "titulo": "Unidad 1",
    "descripcion": "Conversión de bases, números primos y Fibonacci",
    "carpeta": "unidad1",
    "trabajos": [
        trabajo("binario", "01_Binario.py", "Decimal a binario", "Divisiones sucesivas entre 2.", binario, CAMPO),
        trabajo("octal", "02_octal.py", "Decimal a octal", "Divisiones sucesivas entre 8.", octal, CAMPO),
        trabajo("hexadecimal", "03_Hexadecimal.py", "Decimal a hexadecimal",
                "Divisiones entre 16 usando la cadena de dígitos 0-F.", hexadecimal, CAMPO),
        trabajo("binario-compacto", "04_binario_compacto.py", "Binario (compacto)",
                "Versión en pocas líneas con asignación múltiple.", binario_compacto, CAMPO),
        trabajo("octal-compacto", "05_octal-compactado.py", "Octal (compacto)",
                "Versión compacta de la conversión a base 8.", octal_compacto, CAMPO),
        trabajo("hexadecimal-compacto", "06_Hexal_compacto.py", "Hexadecimal (compacto)",
                "Versión compacta de la conversión a base 16.", hexadecimal_compacto, CAMPO),
        trabajo("primo", "07_primo.py", "¿Es primo?", "Indica si un número es primo o no.", primo, CAMPO),
        trabajo("primo-fibonacci", "08_primofibonacci.py", "Primo y Fibonacci",
                "Si el número es primo, verifica además si pertenece a la serie de Fibonacci.", primo_fibonacci, CAMPO),
    ],
}
