from django.db import models
from user.models import User

# 운동별 기본값
class TrainInfo(models.Model):
    train_name = models.CharField(max_length=40)
    default_activation = models.TimeField()
    default_break = models.TimeField()
    default_set = models.IntegerField()
    default_calorie = models.IntegerField()

# 유저의 운동 결과 저장
class TrainResult(models.Model):
    activation_time = models.TimeField()
    activation_time = models.TimeField()
    break_time = models.TimeField()
    train_set = models.IntegerField()
    calorie_consumption = models.IntegerField()
    train = models.ForeignKey(TrainInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)