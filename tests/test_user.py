import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = "kennedy", email ="kennedymbithi12@gmail.com", bio = "I am incredible", profile_pic_url = "image_url", password = 'kenny', id = 1 )

    def tearDown(self):
        User.query.delete()
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Kennedy'))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username, 'kennedy')
        self.assertEquals(self.new_user.email, 'kennedymbithi12@gmail.com')
        self.assertEquals(self.new_user.bio, 'I am incredible')
        self.assertEquals(self.new_user.profile_pic_url, 'image_url')
        self.assertEquals(self.new_user.password,'kenny' )