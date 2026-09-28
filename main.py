from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)

DATA_FILE = Path("data.txt")


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form.get("text", "")
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(text + "\n")
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)