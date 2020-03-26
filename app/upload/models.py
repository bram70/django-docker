from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    class Meta:
        permissions = (
            ( "read_book", "Can read book"),
            )
