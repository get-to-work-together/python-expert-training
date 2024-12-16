import unittest

from ..src.models.user import User
from ..src.persistence.user_persistence import *


class TestUser(unittest.TestCase):

    def setUp(self):
        create_database_and_tables(force = True)

    def test_create_database_and_tables(self):
        create_database_and_tables(force = True)
        stored_users = select_users()
        self.assertListEqual([], stored_users)

    def test_insert_user(self):
        username = 'aeinstein'
        user = User(username, 'a.einstein@mit.edu', 'Albert Einstein')

        insert_user(user)

        stored_user = select_user_by_username(username)
        self.assertIsNotNone(stored_user)

    def test_delete_user(self):
        username = 'aeinstein'
        user = User(username, 'a.einstein@mit.edu', 'Albert Einstein')

        insert_user(user)

        delete_user_by_username(username)

        stored_user = select_user_by_username(username)
        self.assertIsNone(stored_user)

    def test_password(self):
        username = 'aeinstein'
        password = 'Welkom01!'
        wrong_password = 'wrong_password'
        user = User(username, 'a.einstein@mit.edu', 'Albert Einstein')

        user.set_password(password)

        insert_user(user)

        stored_user = select_user_by_username(username)

        self.assertTrue(stored_user.validate_password(password))
        self.assertFalse(stored_user.validate_password(wrong_password))

    def test_token(self):
        username = 'aeinstein'
        user = User(username, 'a.einstein@mit.edu', 'Albert Einstein')

        token = user.token

        insert_user(user)

        stored_user = select_user_by_username(username)
        self.assertEqual(token, stored_user.token)

    def test_update(self):
        username = 'aeinstein'
        user = User(username, 'a.einstein@mit.edu', 'Albert Einstein')

        insert_user(user)

        stored_user = select_user_by_username(username)

        stored_user.fullname = 'UPDATED'
        update_user(stored_user)

        stored_user = select_user_by_username(username)
        self.assertEqual('UPDATED', stored_user.fullname)


if __name__ == '__main__':
    unittest.main()

