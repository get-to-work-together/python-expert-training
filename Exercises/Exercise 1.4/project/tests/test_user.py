import unittest

from ..src.models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.username = 'aeinstein'
        self.fullname = 'Albert Einstein'
        self.email = 'a.einstein@mit.edu'
        self.user = User(self.username, self.email, self.fullname)

    def test_instantiation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.username, self.user.username)
        self.assertEqual(self.fullname, self.user.fullname)
        self.assertEqual(self.email, self.user.email)

    def test_password(self):
        password = 'Welkom!123'
        wrong_password = 'WrongPassword'
        self.user.set_password(password)
        self.assertTrue(self.user.validate_password(password))
        self.assertFalse(self.user.validate_password(wrong_password))

    def test_email(self):
        with self.assertRaises(Exception):
            self.user.email = 'invalid-email'

    def test_token(self):
        self.assertIsNotNone(self.user.token)
        self.assertIsInstance(self.user.token, str)


if __name__ == '__main__':
    unittest.main()
