from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.name
