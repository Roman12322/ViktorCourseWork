from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)

class Results(models.Model):
    userId = models.CharField(max_length=50)
    sequence1 = models.CharField(max_length=100)
    sequence2 = models.CharField(max_length=100)
    result = models.IntegerField()