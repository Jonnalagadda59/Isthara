from django.db import models

class RegistrationData(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    mobile = models.BigIntegerField()