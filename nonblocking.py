from flask import Flask, request, jsonify
import aiosqlite
import asyncio

app = Flask(__name__)

@app.route("/users", methods=["POST"])
async def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    async with aiosqlite.connect("users.db") as db:
        await db.execute("INSERT INTO users (name) VALUES (?)", (data["name"],))
        await db.commit()

    return jsonify({"message": f"User {data['name']} created."})

if __name__ == "__main__":
    import hypercorn.asyncio
    import hypercorn.config

    config = hypercorn.config.Config()
    config.bind = ["0.0.0.0:8001"]
    asyncio.run(hypercorn.asyncio.serve(app, config))
