from flask import Flask, jsonify

app = Flask(
    __name__,
    static_folder="static",
    static_url_path=""
)

@app.get("/")
def inicio():
    return app.send_static_file("index.html")

@app.get("/api/config")
def ontener_configuracion():
    datos = {
        "titulo": "Panel de Periféricos",
        "boton": "Ingresar",
        "enlace": {
            "texto": "Ver datos JSON",
            "url": "/api/config"
        },
        "Imagen": {
            "src": "/imagenes/logo.png",
            "alt": "ingenieria"
        },
        "menu": ["Inicio", "Formulario", "Ayuda"]
    }
    return jsonify(datos)

if __name__ == "__main__":
    app.run(debug=True)