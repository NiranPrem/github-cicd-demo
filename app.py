from flask import Flask, jsonify
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "GitHub CI/CD Demo",
        "status": "Running",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "Development"),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
