from flask import Flask, request, jsonify, render_template
from nlp_parser import parse_command
from mqtt_control import send_mqtt_command

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    parsed = parse_command(data["command"])
    if parsed["action"] and parsed["device"] and parsed["location"]:
        message = send_mqtt_command(parsed["location"], parsed["device"], parsed["action"])
        return jsonify({"message": message})
    else:
        return jsonify({"message": "Could not understand the command."})

if __name__ == "__main__":
    app.run(debug=True)