from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "players": [],
    "player_count": 0,
    "global_message": ""
}

@app.route("/")
def home():
    return "Server is running"

@app.route("/update_players", methods=["POST"])
def update_players():
    json_data = request.get_json()
    if json_data:
        data["players"] = json_data.get("players", [])
        data["player_count"] = json_data.get("player_count", 0)
    return jsonify({"status": "ok"})

@app.route("/get_players", methods=["GET"])
def get_players():
    return jsonify({
        "players": data["players"],
        "player_count": data["player_count"]
    })

@app.route("/send_command", methods=["POST"])
def send_command():
    json_data = request.get_json()
    if json_data and "global_message" in json_data:
        data["global_message"] = json_data["global_message"]
    return jsonify({"status": "ok"})

@app.route("/get_commands", methods=["GET"])
def get_commands():
    cmd = {"global_message": data["global_message"]}
    data["global_message"] = ""
    return jsonify(cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)