import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Página principal con formulario
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            resultado = a + b
        except:
            resultado = "Error: Ingresa números válidos."

    return render_template_string("""
        <html>
            <head>
                <title>Suma de 2 Números</title>
            </head>
            <body style="font-family: sans-serif; padding: 20px;">
                <h2>Sumar dos números</h2>
                <form method="POST">
                    Número 1: <input type="text" name="a"><br><br>
                    Número 2: <input type="text" name="b"><br><br>
                    <input type="submit" value="Sumar">
                </form>
                {% if resultado is not none %}
                    <h3>Resultado: {{ resultado }}</h3>
                {% endif %}
            </body>
        </html>
    """, resultado=resultado)

# API para consumo externo
@app.route("/sumar")
def sumar():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"resultado": a + b})
    except:
        return jsonify({"error": "Parámetros inválidos"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
