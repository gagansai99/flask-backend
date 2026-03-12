from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask Backend Running"

@app.route("/api/message", methods=["POST"])
def message():

    data = request.json
    text = data["text"]

    return jsonify({
        "response": f"Server received: {text}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)