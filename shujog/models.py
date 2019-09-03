from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50, null=True)
