"""Unidad 2: condiciones, ciclos, operadores lógicos, validación, login y cajero."""
from .ayuda import SI_NO, decimal, entero, numero, trabajo


# --- 01 a 05: condiciones, operadores y for ---------------------------------
def condiciones(v):                                    # 01_Condiciones.py
    return [str(bool(x)) for x in (1, 0, -1, 10000, 10.5, "A")]


def operadores(v):                                     # 02_Operadores.py
    op = v["operador"]
    a, b = numero(v["o1"]), numero(v["o2"])
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        r = a / b
    else:
        raise ValueError("Operador no válido.")
    return [str(r)]


def for_cuadrados(v):                                  # 03_For.py
    return [f"{n} {n ** 2}" for n in range(0, 7, 3)]


def for_pares(v):                                      # 04_For1-100.py
    return [str(n) for n in range(0, 101, 2)]


def for_primo(v):                                      # 05_For1-100_primo.py
    return [f"{n} {n % 2 != 0 or n % 3 != 0 or n % 5 != 0 or n % 7 != 0}" for n in range(1, 101, 2)]


# --- 06: reto propina --------------------------------------------------------
def reto_propina(v):                                   # 06_Reto.py
    total = decimal(v["total"], minimo=0, msg="Escribe un total válido (mayor o igual a 0).")
    propina = decimal(v["propina"], minimo=0, msg="Escribe un porcentaje válido (mayor o igual a 0).")
    n = entero(v["personas"], minimo=1, msg="El número de personas debe ser un entero de 1 en adelante.")
    return [f"La propina es: {total * propina / 100}",
            f"La propina por persona es: {total * propina / 100 / n:.2f}"]


# --- 07 y 08: operadores lógicos ----------------------------------------------
def _datos_autorizacion(v):
    edad = entero(v["edad"], 0, 150, "La edad debe ser un entero entre 0 y 150.")
    return edad, v["credencial"] == "si", v["adeudo"] == "si"


def logicos(v):                                        # 07_Operadores_logicos.py
    edad, tiene_credencial, tiene_adeudo = _datos_autorizacion(v)
    es_mayor = edad >= 18
    documento_valido = tiene_credencial
    sin_adeudo = not tiene_adeudo
    autorizado = es_mayor and documento_valido and sin_adeudo
    return [str(autorizado)]


def if_logicos(v):                                     # 08_if_operadores_logicos.py
    edad, tiene_credencial, tiene_adeudo = _datos_autorizacion(v)
    if edad >= 18:
        es_mayor = True
    else:
        es_mayor = False
    documento_valido = tiene_credencial
    if not tiene_adeudo:
        sin_adeudo = True
    else:
        sin_adeudo = False
    if es_mayor and documento_valido and sin_adeudo:
        autorizado = True
    else:
        autorizado = False
    return [str(autorizado)]


# --- 09 a 13: break/continue, while y validaciones ----------------------------
def break_continue(v):                                 # 09_break-continue.py
    salida = []
    for numero_ in [4, 7, 9, 12]:
        if numero_ == 9:
            continue
        salida.append(f"con continue {numero_}")
    for numero_ in [4, 7, 9, 12]:
        if numero_ == 9:
            break
        salida.append(f"con break {numero_}")
    return salida


def while_break(v):                                    # 10_while-break.py
    opcion = v["opcion"].strip().upper()
    if opcion in ["A", "B", "C"]:
        return [f"Elegiste opción {opcion}"]
    return ["Opción inválida. Intenta de nuevo"]


def try_except(v):                                     # 11_tryexcept.py
    try:
        edad = int(v["edad"])
        if 0 <= edad <= 120:
            return [f"Edad registrado: {edad}"]
        return ["La edad debe estar entre 0 y 120 años."]
    except ValueError:
        return ["Escribe un numero entero."]


def sin_try_except(v):                                 # 12_sintryexcept.py
    texto = v["edad"]
    try:
        edad = int(texto)
    except ValueError:
        return ["Traceback (most recent call last):",
                '  File "12_sintryexcept.py", line 2, in <module>',
                f"ValueError: invalid literal for int() with base 10: {texto!r}",
                "",
                "(el programa se cierra con error)"]
    if 0 <= edad <= 120:
        return [f"Edad registrada: {edad}"]
    return ["La edad debe estar entre 0 y 120 años."]


def validar_nombre(v):                                 # 13_strval.py
    nombre = v["nombre"].strip()
    nombre = " ".join(nombre.split())
    if nombre and nombre.replace(" ", "").isalpha():
        return [f"Hola, {nombre.title()}"]
    return ["Usa letras y no dejes el nombre vacio."]


# --- 14 y 15: login -----------------------------------------------------------
USUARIO = "alumno"
CLAVE = "python123"


def login(v):                                          # 14_login.py
    usuario = v["usuario"].strip().lower()
    if usuario == USUARIO and v["clave"] == CLAVE:
        return ["Bienvenido"]
    return ["Credenciales incorrectas"]


def login_intentos(v):                                 # 15_login.py
    salida, intentos = [], 0
    for i in range(1, 4):
        usuario, clave = v[f"u{i}"], v[f"c{i}"]
        if not usuario.strip() and not clave:
            continue
        intentos += 1
        if usuario.strip().lower() == USUARIO and clave == CLAVE:
            salida.append("Bienvenido")
            return salida
        salida.append("Credenciales incorrectas")
    if intentos == 3:
        salida.append("Acceso bloqueado")
    return salida


# --- 16 y 17: cajero ------------------------------------------------------------
MENU = ["Bienvenido al cajero automatico", "1. Consultar saldo", "2. Depositar", "3. Retirar", "4. Salir"]
ACCIONES = {"1": "Saldo: $0.00 ", "2": "Deposito realizado", "3": "Retiro realizado",
            "4": "Saliendo del cajero automatico..."}


def cajero(v):                                         # 16_cajero.py (corregido)
    opcion = v["opcion"].strip()
    return MENU + [f"Opcion: {opcion}", ACCIONES.get(opcion, "Opcion invalida")]


def reto_cajero(v):                                    # 17_reto_cajero.py
    if v["usuario"].strip().lower() != USUARIO or v["clave"] != CLAVE:
        return ["Credenciales incorrectas"]
    opcion = v["opcion"].strip()
    salida = MENU + [f"Opcion: {opcion}"]
    if opcion in ACCIONES:
        salida.append(ACCIONES[opcion])
    else:
        salida += MENU
    return salida


# --- campos de formulario ---------------------------------------------------------
OPCION = {"name": "opcion", "label": "Opción", "type": "text", "valor": "1"}
LOGIN = [{"name": "usuario", "label": "Usuario", "type": "text", "valor": "alumno"},
         {"name": "clave", "label": "Contraseña", "type": "password"}]
INTENTOS = []
for _i in (1, 2, 3):
    INTENTOS += [{"name": f"u{_i}", "label": f"Intento {_i}: usuario", "type": "text",
                  "requerido": _i == 1, "valor": "alumno" if _i == 1 else ""},
                 {"name": f"c{_i}", "label": f"Intento {_i}: contraseña", "type": "password",
                  "requerido": _i == 1}]
AUT = [{"name": "edad", "label": "Edad", "type": "number", "valor": "19"},
       {"name": "credencial", "label": "¿Tiene credencial?", "type": "select", "opciones": SI_NO, "valor": "si"},
       {"name": "adeudo", "label": "¿Tiene adeudo?", "type": "select", "opciones": SI_NO, "valor": "no"}]

UNIDAD = {
    "titulo": "Unidad 2",
    "descripcion": "Condiciones, ciclos, operadores lógicos, validación, login y cajero",
    "carpeta": "unidad2",
    "trabajos": [
        trabajo("condiciones", "01_Condiciones.py", "Valores booleanos",
                "bool() de distintos valores: todo distinto de cero es True.", condiciones),
        trabajo("operadores", "02_Operadores.py", "Calculadora con operadores",
                "Aplica +, -, * o / a dos números.", operadores,
                [{"name": "operador", "label": "Operador", "type": "select",
                  "opciones": [("+", "+  suma"), ("-", "-  resta"), ("*", "*  multiplicación"), ("/", "/  división")],
                  "valor": "+"},
                 {"name": "o1", "label": "Primer número", "type": "number", "step": "any", "valor": ""},
                 {"name": "o2", "label": "Segundo número", "type": "number", "step": "any", "valor": ""}]),
        trabajo("for-cuadrados", "03_For.py", "For con range y cuadrados",
                "Recorre range(0, 7, 3) e imprime cada número con su cuadrado.", for_cuadrados),
        trabajo("for-pares", "04_For1-100.py", "Pares del 0 al 100",
                "Ciclo for con paso de 2.", for_pares),
        trabajo("for-primo", "05_For1-100_primo.py", "For impares y 'primo'",
                "Recorre los impares del 1 al 99 evaluando una condición.", for_primo),
        trabajo("reto-propina", "06_Reto.py", "Reto: propina por persona",
                "Calcula la propina total y por persona.", reto_propina,
                [{"name": "total", "label": "Total de la cuenta", "type": "number", "step": "any", "valor": ""},
                 {"name": "propina", "label": "Porcentaje de propina", "type": "number", "step": "any", "valor": "10"},
                 {"name": "personas", "label": "Número de personas", "type": "number", "valor": "1"}]),
        trabajo("operadores-logicos", "07_Operadores_logicos.py", "Operadores lógicos",
                "Autorización con and y not.", logicos, AUT),
        trabajo("if-logicos", "08_if_operadores_logicos.py", "If con operadores lógicos",
                "La misma autorización escrita con if/else.", if_logicos, AUT),
        trabajo("break-continue", "09_break-continue.py", "break y continue",
                "Diferencia entre saltar un elemento y terminar el ciclo.", break_continue),
        trabajo("while-break", "10_while-break.py", "While con break",
                "Pide A, B o C; en el original repite hasta que sea válida.", while_break,
                [{"name": "opcion", "label": "Elige A, B o C", "type": "text", "valor": ""}]),
        trabajo("try-except", "11_tryexcept.py", "Validar con try/except",
                "Edad entera entre 0 y 120 atrapando ValueError.", try_except,
                [{"name": "edad", "label": "Edad (prueba con un número o con texto)", "type": "text", "valor": ""}]),
        trabajo("sin-try-except", "12_sintryexcept.py", "Sin try/except",
                "Misma validación pero sin manejar el error.", sin_try_except,
                [{"name": "edad", "label": "Edad (prueba con un número o con texto)", "type": "text", "valor": ""}]),
        trabajo("validar-nombre", "13_strval.py", "Validar nombre",
                "Solo letras, sin espacios repetidos, formato título.", validar_nombre,
                [{"name": "nombre", "label": "Nombre", "type": "text", "valor": ""}]),
        trabajo("login", "14_login.py", "Login",
                "Compara usuario y contraseña (usuario: alumno, contraseña: python123).", login, LOGIN),
        trabajo("login-intentos", "15_login.py", "Login con 3 intentos",
                "Hasta 3 intentos; si todos fallan, bloquea el acceso.", login_intentos, INTENTOS),
        trabajo("cajero", "16_cajero.py", "Cajero (versión con errores)",
                "Menú de cajero con funciones.", cajero, [OPCION]),
        trabajo("reto-cajero", "17_reto_cajero.py", "Reto: cajero con login",
                "Login y luego el menú del cajero.", reto_cajero, LOGIN + [OPCION]),
    ],
}
