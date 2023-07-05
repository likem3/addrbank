from cryptography.fernet import Fernet
import base64, hashlib


def str_to_base64(data: str):
    return base64.b64encode(
        data.encode("ascii")
    ).decode("ascii")


def fernet_key(data: str) -> bytes:
    key = data.encode("utf-8")
    assert isinstance(key, bytes)
    hlib = hashlib.md5()
    hlib.update(key)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('utf-8'))