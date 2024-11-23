#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request
from auth import Auth
import requests


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """return JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """register user if not exist"""
    email = request.form["email"]
    password = request.form["password"]
    if AUTH.register_user(email, password):
        return jsonify({"email": email, "message": "user created"})
    else:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"])
def login():
    """user logging"""
    email = request.form["email"]
    password = request.form["password"]
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        return jsonify({f"email": email, "message": "logged in"})
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
