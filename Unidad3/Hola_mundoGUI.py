from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return f"""
    <h1>Camellonaldo</h1>
    <img src="{url_for('static', filename='messi.png')}" alt="Imagen VS" width="500">
    """

if __name__ == '__main__':
    app.run(debug=True)