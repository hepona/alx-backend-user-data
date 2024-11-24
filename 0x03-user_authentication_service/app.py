#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, make_response, abort, redirect
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
        jso = jsonify({"email": email, "message": "logged in"}), 200
        resp = make_response(jso)
        resp.set_cookie("session_id", AUTH.create_session(email))
        return resp
    abort(401)


@app.route("/session", methods=["DELETE"])
def logout():
    """user's logout"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/", 302)
    abort(403)


@app.route("/profile")
def profile():
    """user profile"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
