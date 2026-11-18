# Menú de trabajos (Flask)

Cada trabajo es una opción del menú, organizado por unidad.

    menu_flask/
    ├── app.py                  rutas de Flask (arranca el servidor)
    ├── requirements.txt
    ├── README.md
    ├── .vscode/launch.json     botón ▶ de VS Code (F5)
    ├── unidades/
    │   ├── __init__.py         registro de las unidades
    │   ├── ayuda.py            validaciones y helper trabajo()
    │   ├── unidad1.py          8 trabajos: bases, primos, Fibonacci
    │   └── unidad2.py          17 trabajos: condiciones, ciclos, login, cajero
    ├── trabajos/               tus .py originales (se muestran en pantalla)
    │   ├── unidad1/
    │   └── unidad2/
    ├── templates/              base, index, unidad, trabajo
    └── static/                 style.css (estilos) y app.js (botón Limpiar)

## Ejecutar en Visual Studio Code
1. File > Open Folder... y elige `menu_flask`.
2. Terminal > New Terminal:

       python -m venv .venv
       .venv\Scripts\activate          (Windows)
       pip install -r requirements.txt
       python app.py

   (o presiona F5 para correrlo desde el depurador)
3. Abre http://127.0.0.1:5000

## Para agregar un trabajo nuevo
1. Copia el .py a `trabajos/unidadN/`.
2. En `unidades/unidadN.py` agrega un `trabajo(...)` con su función y sus campos.
