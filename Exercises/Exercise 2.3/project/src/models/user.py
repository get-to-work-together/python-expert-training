import base64
from datetime import datetime
import hashlib
import uuid
import re
import secrets


class User:

    def __init__(self, username: str, email: str, fullname: str):
        self._id = None
        self._username = username
        self._email = None
        self._fullname = fullname
        self._salt = secrets.token_urlsafe(30)
        self._password_hash = None
        self._token = None

        self.email = email
        self.generate_token()

    def __repr__(self) -> str:
        return f'User("{self._username}", "{self._email}", "{self._fullname}")'

    @property
    def id(self) -> str:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def fullname(self) -> str:
        return self._fullname

    @property
    def salt(self) -> str:
        return self._salt

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @property
    def token(self) -> str:
        return self._token

    @id.setter
    def id(self, value: int):
        self._id = value

    @fullname.setter
    def fullname(self, value: int):
        self._fullname = value

    @email.setter
    def email(self, value: str):
        pattern = r'^[\w\.]+@[\w\.]+\.[a-zA-Z]{2,3}$'
        if re.match(pattern, value):
            self._email = value
        else:
            raise Exception('Invalid format for e-mail.')

    @salt.setter
    def salt(self, value: str):
        self._salt = value

    @password_hash.setter
    def password_hash(self, value: str):
        self._password_hash = value

    @token.setter
    def token(self, value: str):
        self._token = value

    @staticmethod
    def _hash_password(password: str, salt: bytes) -> bytes:
        t_sha = hashlib.sha512()
        t_sha.update(bytes(password, encoding='utf8') + salt)
        return base64.urlsafe_b64encode(t_sha.digest())

    def set_password(self, password: str):
        salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        hashed_password = self._hash_password(password, salt)
        self._salt = salt
        self._password_hash = hashed_password

    def validate_password(self, password: str) -> bool:
        salt = self._salt
        stored_hashed_password = self._password_hash
        if salt and stored_hashed_password:
            hashed_password = self._hash_password(password, salt)
            if hashed_password == stored_hashed_password:
                return True
            else:
                return False
        else:
            raise Exception('No password set yet.')

    def generate_token(self):
        self._token = secrets.token_urlsafe()
