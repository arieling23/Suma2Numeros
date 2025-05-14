from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sumar", methods=["GET"])
def sumar():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        resultado = a + b
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Parámetros inválidos"}), 400

if __name__ == "__main__":
    app.run(debug=True)
