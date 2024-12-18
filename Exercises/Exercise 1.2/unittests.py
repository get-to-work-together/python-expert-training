from user import User
import unittest

class TestUser(unittest.TestCase):

    def test_instantiation(self):
        # AAA - Arange, Action, Assert
        user = User(username='peteranema',
                    email='peter.anema@tip.nl',
                    fullname='Peter Anema')

        self.assertTrue( isinstance(user, User) )

    def test_properties(self):
        user = User(username='peteranema',
                    email='peter.anema@tip.nl',
                    fullname='Peter Anema')

        self.assertEqual( 'peteranema', user.username )
        self.assertEqual( 'peter.anema@tip.nl', user.email )
        self.assertEqual( 'Peter Anema', user.fullname )

    def test_password(self):
        user = User(username='peteranema',
                    email='peter.anema@tip.nl',
                    fullname='Peter Anema')

        password = 'Welkom01!'
        user.set_password(password)
        self.assertTrue(  user.validate_password(password) )
        self.assertFalse( user.validate_password('XX') )


if __name__ == '__main__':
    unittest.main()