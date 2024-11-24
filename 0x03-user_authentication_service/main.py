#!/usr/bin/env python3
"""20. End-to-end integration test"""
import requests

url = "http://localhost:5000"


def resp():
    r = requests.post(
        f"{url}/users", data={"email": email, "password": password})
    return r


def register_user(email: str, password: str) -> None:
    """test function"""

    assert resp().status_code == 200
    assert resp().json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """test function"""
    assert resp().statue_code == 401


def log_in(email: str, password: str) -> str:
    """test function"""
    assert resp().status_code == 200
    assert resp().json() == {"email": email, "message": "logged in"}
    assert resp().cookies.get("session_id")


def profile_unlogged() -> None:
    """test function"""
    assert resp().status_code == 403


def profile_logged(session_id: str) -> None:
    """test function"""
    assert resp().status_code == 200


def log_out(session_id: str) -> None:
    """test function"""
    assert resp().status_code == 302


def reset_password_token(email: str) -> str:
    """test function"""
    assert resp().status_code == 403
    assert resp().json() == {"email": email, "reset_token": token}


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """test function"""
    assert resp().status_code == 200
    assert resp().json() == {
        "email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
