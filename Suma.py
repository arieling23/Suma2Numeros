import os
from flask import Flask, request, jsonify

app = Flask(__name__)

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
