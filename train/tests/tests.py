from django.test import TestCase
from user.models import User
from train.models import TrainInfo, TrainResult
from django.test import Client
import json

class TrainTest(TestCase):

    def setUp(self):

        TrainInfo(
            train_name="pushpush",
            default_activation="0:00:01",
            default_break="0:00:05",
            default_set=4,
            default_calorie=777,
        ).save()

        TrainInfo(
            train_name="downup",
            default_activation="0:00:03",
            default_break="0:00:07",
            default_set=1,
            default_calorie=555,
        ).save()
        
        TrainInfo(
            train_name="push",
            default_activation="0:00:01",
            default_break="0:00:05",
            default_set=3,
            default_calorie=777,
        ).save()

        TrainInfo(
            train_name="push1",
            default_activation="0:00:01",
            default_break="0:00:05",
            default_set=4,
            default_calorie=77,
        ).save()

        c = Client()
        test     = {'user_email':'kim2@gmail.com', 'user_password':'qwer1234','user_nickname':'heybo22y'}
        response = c.post('/user/', json.dumps(test), content_type="application/json")
        
    def test_user_can_get_train_infos(self):
        c = Client()

        response     = c.get('/train/all', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_post_train_results(self):
        c = Client()
        test         = {'user_email':'kim2@gmail.com', 'user_password':'qwer1234'}
        response     = c.post('/user/signin', json.dumps(test), content_type="application/json")
        access_token = response.json()['access_token']

        parameter         = {  
            "activation_time":"00:01:18",
            "break_time":"00:01:18",
            "train_set":2,
            "calorie_consumption":65566,
            "train_id":1
            }

        response     = c.post('/train', json.dumps(parameter), **{'HTTP_AUTHORIZATION':access_token, 'content_type':"application/json"})
        self.assertEqual(response.status_code, 200)
   

    def tearDown(self):
        User.objects.filter(user_email ='kim@gmail.com').delete()