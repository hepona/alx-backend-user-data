#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string."""
    pw_bite = password.encode()
    return bcrypt.hashpw(pw_bite, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
