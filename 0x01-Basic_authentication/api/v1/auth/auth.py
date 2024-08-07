#!/usr/bin/env python3
"""3. Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentification class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        pass

    def current_user(self, request=None) -> TypeVar("User"):
        """current_user"""
        pass
