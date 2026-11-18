"""Menú de trabajos por unidad (Flask).

Estructura:
  app.py                  -> rutas de Flask (no necesitas tocarlo)
  unidades/unidad1.py     -> trabajos de la Unidad 1
  unidades/unidad2.py     -> trabajos de la Unidad 2
  trabajos/unidadN/*.py   -> tus archivos originales (se muestran en pantalla)
"""
from pathlib import Path
from flask import Flask, render_template, request, abort

from unidades import UNIDADES

app = Flask(__name__)
BASE = Path(__file__).parent


def leer_codigo(unidad, trabajo):
    ruta = BASE / "trabajos" / unidad["carpeta"] / trabajo["archivo"]
    if not ruta.exists():
        return "(archivo no encontrado)"
    datos = ruta.read_bytes()
    for enc in ("utf-8", "cp1252"):
        try:
            return datos.decode(enc).replace("\r\n", "\n").strip()
        except UnicodeDecodeError:
            pass
    return datos.decode("latin-1")


def buscar(num_unidad, id_trabajo):
    unidad = UNIDADES.get(num_unidad)
    if not unidad:
        abort(404)
    for t in unidad["trabajos"]:
        if t["id"] == id_trabajo:
            return unidad, t
    abort(404)


@app.context_processor
def inyectar_unidades():
    return {"unidades_nav": UNIDADES}


@app.route("/")
def inicio():
    return render_template("index.html", unidades=UNIDADES)


@app.route("/unidad/<int:num>")
def unidad(num):
    u = UNIDADES.get(num)
    if not u:
        abort(404)
    return render_template("unidad.html", num=num, unidad=u)


@app.route("/unidad/<int:num>/<id_trabajo>", methods=["GET", "POST"])
def trabajo(num, id_trabajo):
    u, t = buscar(num, id_trabajo)
    campos = t["campos"]
    valores = {c["name"]: c.get("valor", "") for c in campos}
    salida, error = None, None
    if request.method == "POST":
        for c in campos:
            valores[c["name"]] = request.form.get(c["name"], "")
        try:
            salida = t["func"](valores)
        except ValueError as e:
            error = str(e) or "Datos no válidos."
    return render_template("trabajo.html", num=num, unidad=u, trabajo=t,
                           codigo=leer_codigo(u, t), valores=valores,
                           salida=salida, error=error)


if __name__ == "__main__":
    app.run(debug=True)
