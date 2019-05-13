from ..models import User
from django.test import TestCase
from django.test import Client
import json


class UserSignInCase(TestCase):
    def setUp(self):
        # User.objects.create(user_email="ppp@gmail.com", user_nickname="yona", user_password="abcd1234")
        pass

    def tearDown(self):
        pass
  
    def test_user_can_sign_in(self):
        c = Client()
        response = c.post('/user/signin', json.dumps({"user_email": "kim@gmail.com", "user_password": "qwer1234"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)

class UserSignUpCase(TestCase):
    def setUp(self):
        # User.objects.create(user_email="ppp@gmail.com", user_nickname="yona", user_password="abcd1234")
        pass
        
    def tearDown(self):
        pass
  
    def test_user_can_sign_up(self):
        c = Client()
        response = c.post('/user', json.dumps({"user_email": "kids3m@gmail.com", "user_nickname": "heyhey","user_password": "qwer1234"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)