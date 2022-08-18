from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

class Predict(models.Model):
    email = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_key')
    time = models.CharField(max_length = 200)
    emotion = models.IntegerField

class Asmr(models.Model):
    emotion = models.IntegerField()
    file = models.FileField(null=True)

class Video(models.Model):
    emotion = models.IntegerField()
    url = models.URLField()

