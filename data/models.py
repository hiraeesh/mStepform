from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
