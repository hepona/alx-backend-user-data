#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """return JSON payload"""
    return jsonify({"message": "Bienvenue"}, 200)


@app.route("/users", methods=["POST"])
def users(email, password) -> Response:
    """register user if not exist"""

    if AUTH.register_user(email, password):
        return jsonify({f"email": "{email}", "message": "user created"})
    else:
        return jsonify({"message": "email already registered"}, 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
