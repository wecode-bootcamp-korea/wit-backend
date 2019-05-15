from django.db import models
# from train.models import TrainInfo

# 유저 필수입력값
class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_password = models.CharField(max_length=200)

# 유저 선택입력값
class UserDetail(models.Model):
    user_sex = models.BooleanField()
    user_birthdate = models.DateField()
    user_weight = models.DecimalField(decimal_places=1, max_digits=4)
    user_height = models.DecimalField(decimal_places=1, max_digits=4)
    user_smoking = models.BooleanField()
    user_preference = models.ForeignKey(to='train.TrainInfo', on_delete=models.CASCADE)