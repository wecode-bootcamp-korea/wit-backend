from django.db import models
from train.models import TrainInfo, TrainResult

# 유저 필수입력값
class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_password = models.CharField(max_length=200)
    user_preference = models.ManyToManyField(TrainInfo)
    user_result = models.ManyToManyField(TrainInfo, through='train.TrainResult', related_name='user_traininfo_fk')

# 유저 선택입력값
class UserDetail(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    user_sex = models.BooleanField()
    user_birthdate = models.DateField()
    user_weight = models.DecimalField(decimal_places=1, max_digits=4)
    user_height = models.DecimalField(decimal_places=1, max_digits=4)
