from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete


from ..models.users import User


engine = create_engine('sqlite:///project.db', echo=True)


class Base(DeclarativeBase):
    pass


class UserDB(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150))
    fullname: Mapped[Optional[str]]
    salt: Mapped[Optional[str]]
    password_hash: Mapped[Optional[str]]
    token: Mapped[Optional[str]]


def from_user(user: User) -> UserDB:
    if user:
        userdb = UserDB(id = user.id,
                        username = user.username,
                        email = user.email,
                        fullname = user.fullname,
                        salt = user.salt,
                        password_hash = user.password_hash,
                        token = user.token)
        return userdb


def to_user(userdb: UserDB) -> User:
    if userdb:
        user = User(userdb.username,
                    userdb.email,
                    userdb.fullname)
        user.id = userdb.id
        user.salt = userdb.salt
        user.password_hash = userdb.password_hash
        user.token = userdb.token
        return user


def create_database_and_tables(force = False):
    if force:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def insert_user(user: User):
    userdb = from_user(user)
    with Session(engine) as session:
        session.add(userdb)
        session.commit()


def select_users():
    with Session(engine) as session:
        stmt = select(UserDB)
        return [to_user(userdb) for userdb in session.scalars(stmt)]


def select_user_by_username(username: str):
    with Session(engine) as session:
        stmt = select(UserDB).where(UserDB.username == username)
        return to_user(session.scalar(stmt))


def select_user_by_id(id_: int):
    with Session(engine) as session:
        stmt = select(UserDB).where(UserDB.id == id_)
        return to_user(session.scalar(stmt))


def select_user_by_token(token: str):
    with Session(engine) as session:
        stmt = select(UserDB).where(UserDB.token == token)
        return to_user(session.scalar(stmt))



def delete_user_by_username(username: str):
    with engine.begin() as conn:
        stmt = (delete(UserDB)
                .where(UserDB.username == username))
        result = conn.execute(stmt)


def update_user(user: User):
    username = user.username
    with engine.begin() as conn:
        stmt = (update(UserDB)
                .where(UserDB.username == username)
                .values(email = user.email,
                        fullname=user.fullname,
                        salt = user.salt,
                        password_hash = user.password_hash,
                        token = user.token))
        result = conn.execute(stmt)


def seed():
    users = [
        {'username': 'aeinstein', 'email': 'a.einstein@mit.edu', 'fullname': 'Albert Einstein', 'password': 'Welkom01!'}
    ]

    for d in users:
        user = User(**d)
        insert_user(user)