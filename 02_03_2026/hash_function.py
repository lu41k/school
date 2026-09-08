import os
from hashlib import sha256

SECRET_WORD = "KAMALIN"


def get_hash_password(password: str) -> str:
    return str(sha256((password + SECRET_WORD).encode(encoding="UTF-8")))
