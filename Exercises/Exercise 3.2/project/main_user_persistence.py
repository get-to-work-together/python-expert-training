from django.contrib.auth.password_validation import validate_password

from src.persistence.user_persistence import *


if __name__ == '__main__':

    create_database_and_tables(force = True)

    print(select_users())

    user = User('aeinstein', 'a.einstein@mit.edu', 'Albert Einstein')
    user.set_password('Welkom01!')
    insert_user(user)

    print(select_user_by_username('aeinstein'))

    print(select_user_by_id(1))

    user = select_user_by_id(2)
    user.fullname = 'User met Token'
    token = user.token

    update_user(user)

    print(select_user_by_token(token))

    delete_user_by_username('aeinstein')

    print(select_user_by_username('aeinstein'))

