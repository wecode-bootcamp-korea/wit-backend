from django.db import models


class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)