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


@app.route("/data", methods=["GET"])   # ← потом используем app в декораторе
def get_data():
    if not DATA_FILE.exists():
        return jsonify({"content": []})

    lines = DATA_FILE.read_text(encoding="utf-8").splitlines()
    index = request.args.get("index", "").strip()

    if index == "" or index == "0":
        return jsonify({"content": lines})

    try:
        i = int(index)
    except ValueError:
        return jsonify({"error": "Номер должен быть целым числом"}), 400

    if i < 0 or i > len(lines):
        return jsonify({"error": f"Записи с номером {i} нет. Всего записей: {len(lines)}"}), 404

    return jsonify({"content": [lines[i - 1]]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)