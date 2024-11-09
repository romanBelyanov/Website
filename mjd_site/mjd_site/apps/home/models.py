from django.db import models

class Signin(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    age = models.IntegerField()
    floor = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
