#!/usr/bin/env python3
""" Authentification"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from  sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """take pwd and return bytes"""
    byte = password.encode("utf-8")
    hash = bcrypt.hashpw(byte, bcrypt.gensalt())
    return hash


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register users"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd.decode("utf-8"))
            return user
