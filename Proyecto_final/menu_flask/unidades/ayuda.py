"""Funciones de apoyo para definir trabajos y validar los datos del formulario."""
import math

SI_NO = [("si", "Sí"), ("no", "No")]


def entero(texto, minimo=None, maximo=None, msg="Escribe un número entero."):
    try:
        n = int(str(texto).strip())
    except ValueError:
        raise ValueError(msg)
    if (minimo is not None and n < minimo) or (maximo is not None and n > maximo):
        raise ValueError(msg)
    return n


def decimal(texto, minimo=None, msg="Escribe un número válido."):
    try:
        n = float(str(texto).strip())
    except ValueError:
        raise ValueError(msg)
    if not math.isfinite(n) or (minimo is not None and n < minimo):
        raise ValueError(msg)
    return n


def numero(texto, msg="Escribe un número válido (por ejemplo 8 o 3.5)."):
    """Devuelve int si se puede; si no, float."""
    try:
        return int(str(texto).strip())
    except ValueError:
        return decimal(texto, msg=msg)


def trabajo(id, archivo, titulo, descripcion, func=None, campos=None):
    """Define un trabajo del menú. archivo: nombre del .py original en trabajos/<unidad>/."""
    return {"id": id, "archivo": archivo, "titulo": titulo, "descripcion": descripcion,
            "func": func, "campos": campos or []}
