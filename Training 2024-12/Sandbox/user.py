from typing import List
from typing import Optional
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import base64
from datetime import datetime
import hashlib
import uuid
import re
import secrets


class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"
    _id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    _username: Mapped[str] = mapped_column(String(30), unique=True, name="username")
    _email: Mapped[str] = mapped_column(String(80), name="email")
    _fullname: Mapped[str] = mapped_column(String(200), name="fullname")
    _salt: Mapped[str] = mapped_column(String(80), name="salt", nullable=True)
    _password_hash: Mapped[str] = mapped_column(String(200), name="password_hash", nullable=True)
    _token: Mapped[str] = mapped_column(String(80), name="token", nullable=True)
    active: Mapped[bool] = mapped_column(Boolean(), name="active", default=True)
    created_on: Mapped[datetime] = mapped_column(DateTime(), name="created_on", default=datetime.now())
    last_login_on: Mapped[datetime] = mapped_column(DateTime(), name="last_login_on", nullable=True)
    groups: Mapped[List["Group"]] = relationship("Group", back_populates="user")


    def __init__(self, username: str, email: str, fullname: str):

        self._id = None
        self._username = username
        self._email = None
        self._fullname = fullname
        self._salt = None
        self._password_hash = None
        self._token = None
        self.active = True
        self.created_on = datetime.now()
        self.last_login_on = None
        self.groups = []

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
        return self._fullname.upper()

    @property
    def salt(self) -> str:
        return self._salt

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @property
    def token(self) -> str:
        return self._token

    @email.setter
    def email(self, value: str):
        pattern = r'^[\w\.]+@[\w\.]+\.[a-zA-Z]{2,3}$'
        if re.match(pattern, value):
            self._email = value
        else:
            raise Exception('Invalid format for e-mail.')

    @fullname.setter
    def fullname(self, value: str):
        self._fullname = value

    @staticmethod
    def _hash_password(password: str, salt: bytes) -> bytes:
        sha = hashlib.sha512()
        sha.update(bytes(password, encoding='utf8') + salt)
        return base64.urlsafe_b64encode(sha.digest())

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

    def login(self, password: str) -> bool:
        if self.active and self.validate_password(password):
            self.last_login_on = datetime.now()
            return True
        else:
            return False

    def generate_token(self):
        self._token = secrets.token_urlsafe()

    def validate_token(self, token: str) -> bool:
        return self._token == token

    @staticmethod
    def valid_login(username, password):
        engine = create_engine("sqlite:///users.db", echo=True)
        with Session(engine) as session:
            user = session.query(User).where(User._username == username).first()
            if user and user.validate_password(password):
                return True
            else:
                return False


class Group(Base):

    __tablename__ = "groups"
    _id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    _groupname: Mapped[str] = mapped_column(String(30), name="groupname")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="groups")

    def __init__(self, groupname: str):
        self._id = None
        self._groupname = groupname

    def __repr__(self):
        return f'Group("{self._groupname}")'



if __name__ == '__main__':

    engine = create_engine("sqlite:///users.db", echo=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:

        # user = User(username='peteranema',
        #             email='peter@tip.nl',
        #             fullname='Peter Anema')
        #
        # user.set_password('Welkom01!')

        # user.groups.append(Group('Javascript'))
        # user.groups.append(Group('Python Expert'))
        # user.groups.append(Group('C#'))

        # session.add(user)
        # session.commit()

        # user = User(username='Tijmen',
        #             email='tijmen@gmail.com',
        #             fullname='Tijmen')
        #
        # user.set_password('Welkom01!')
        #
        # user.groups.append(Group('Trombone les'))
        # user.groups.append(Group('Python Expert'))
        # user.groups.append(Group('Dansles'))
        #
        # session.add(user)
        # session.commit()

        # retrieved = session.query(User).where(User._username == 'peteranema').first()
        #
        # print(retrieved)
        #
        # if retrieved and retrieved.validate_password('Welkom01!'):
        #     print('Login SUCCESS!')
        #
        # else:
        #     print('Login FAILED!')
        #
        #
        # session.close()

        print( User.valid_login('peteranema', 'Welkom01!'))
