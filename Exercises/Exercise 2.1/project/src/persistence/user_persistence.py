from ..models.user import User

import sqlite3

db_filename = 'project.db'



def create_database_and_tables(force = False):
    conn = sqlite3.connect(db_filename)

    if force:
        sql = '''DROP TABLE IF EXISTS users;'''
        conn.execute(sql)
        conn.commit()

    sql = '''\
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    fullname VARCHAR(100),
    salt VARCHAR(100),
    password_hash VARCHAR(255),
    token VARCHAR(100),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    '''

    conn.execute(sql)

    conn.commit()

    conn.close()


def insert_user(user: User):
    conn = sqlite3.connect(db_filename)

    sql = '''\
INSERT INTO users (username, email, fullname, salt, password_hash, token)   
VALUES (?, ?, ?, ?, ?, ?);
    '''

    try:
        conn.execute(sql, (user.username,
                           user.email,
                           user.fullname,
                           user.salt,
                           user.password_hash,
                           user.token))

    except Exception as ex:
        print(ex)

    finally:
        conn.commit()
        conn.close()



def select_users():
    conn = sqlite3.connect(db_filename)

    sql = '''\
SELECT * FROM users;'''

    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()

    conn.commit()

    conn.close()

    users = []
    if records:
        for record in records:
            id, username, fullname, email, salt, password_hash, token, created = record

            user = User(username, fullname, email)
            user._salt = salt
            user._password_hash = password_hash
            user._token = token

            users.append(user)

    return users


def select_user_by_username(username: str):
    conn = sqlite3.connect(db_filename)

    sql = '''\
SELECT * FROM users WHERE username=?;'''

    cursor = conn.cursor()
    cursor.execute(sql, (username,))

    record = cursor.fetchone()

    conn.commit()

    conn.close()

    if record:
        id, username, fullname, email, salt, password_hash, token, created = record

        user = User(username, fullname, email)
        user._id = id
        user._salt = salt
        user._password_hash = password_hash
        user._token = token

        return user


def select_user_by_id(id: int):
    conn = sqlite3.connect(db_filename)

    sql = '''\
SELECT * FROM users WHERE id=?;'''

    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    record = cursor.fetchone()

    conn.commit()

    conn.close()

    if record:
        id, username, fullname, email, salt, password_hash, token, created = record

        user = User(username, fullname, email)
        user._id = id
        user._salt = salt
        user._password_hash = password_hash
        user._token = token

        return user


def select_user_by_token(token: str):
    conn = sqlite3.connect(db_filename)

    sql = '''\
SELECT * FROM users WHERE token=?;'''

    cursor = conn.cursor()
    cursor.execute(sql, (token,))

    record = cursor.fetchone()

    conn.commit()

    conn.close()

    if record:
        id, username, fullname, email, salt, password_hash, token, created = record

        user = User(username, fullname, email)
        user._salt = salt
        user._password_hash = password_hash
        user._token = token

        return user



def delete_user_by_username(username: str):
    conn = sqlite3.connect(db_filename)

    sql = 'DELETE FROM users WHERE username=?;'

    cursor = conn.cursor()
    cursor.execute(sql, (username,))

    conn.commit()

    conn.close()



def update_user(user: User):
    if user.id is None:
        insert_user(user)
        return

    conn = sqlite3.connect(db_filename)

    sql = '''\
UPDATE users
SET 
    email = ?,
    fullname = ?,
    salt = ?,
    password_hash = ?,
    token = ?
WHERE id = ?;'''

    cursor = conn.cursor()
    cursor.execute(sql, (user.email,
                         user.fullname,
                         user.salt,
                         user.password_hash,
                         user.token,
                         user.id))

    conn.commit()

    conn.close()
