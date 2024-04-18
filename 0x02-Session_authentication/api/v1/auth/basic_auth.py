#!/usr/bin/env python3
""" 6. Basic auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class.
    """

    def extract_base64_authorization_header(self, ah: str) -> str:
        """ def extract_base64_authorization_header.
        """
        if not ah or type(ah) != str or not ah.startswith("Basic "):
            return
        return "".join(ah.split(" ")[1:])

    def decode_base64_authorization_header(self, b64: str) -> str:
        """ def decode_base64_authorization_header.
        """
        if not b64 or type(b64) != str:
            return
        try:
            b64_bytes = b64.encode('utf-8')
            res = base64.b64decode(b64_bytes)
            return res.decode('utf-8')
        except Exception:
            return

    def extract_user_credentials(self, db64: str) -> (str, str):
        """ def extract_user_credentials.
        """
        if not db64 or type(db64) != str or ":" not in db64:
            return (None, None)
        a, b = db64.split(':')[0], "".join(db64.split(':', 1)[1:])
        return (a, b)
