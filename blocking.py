from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", (data["name"],))
    conn.commit()
    conn.close()

    return jsonify({"message": f"User {data['name']} created."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
