from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the simple Python web server!"

@app.route("/status")
def status():
    return jsonify({"status": "running", "message": "Everything is OK."})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
