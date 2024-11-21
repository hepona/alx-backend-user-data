#!/usr/bin/env python3
""" Authentification"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """take pwd and return bytes"""
    byte = password.encode("utf-8")
    hash = bcrypt.hashpw(byte, bcrypt.gensalt())
    return hash
