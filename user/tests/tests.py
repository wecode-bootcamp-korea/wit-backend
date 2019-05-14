from ..models import User
from django.test import TestCase
from django.test import Client
import json

class UserTest(TestCase):

    def setUp(self):
        c = Client()

        test     = {'user_email':'kim@gmail.com', 'user_password':'qwer1234','user_nickname':'heybo22y'}
        response = c.post('/user/', json.dumps(test), content_type="application/json")
        print(response)

    def test_user_can_signup(self):
        c = Client()
        test     = {'user_email':'test@test.com', 'user_password':'qwer1234', 'user_nickname':'heyboy'}
        response = c.post('/user/', json.dumps(test), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_signin(self):
        c = Client()

        test         = {'user_email':'kim@gmail.com', 'user_password':'qwer1234'}
        user         = User.objects.get(user_email=test['user_email'])
        response     = c.post('/user/signin', json.dumps(test), content_type="application/json")
        access_token = response.json()['access_token']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                response.json(), 
                    {
                        "access_token" : access_token,
                        # "user_email" : user.user_email
                    }
        )
   
    def tearDown(self):
        User.objects.filter(user_email ='kim@gmail.com').delete()
