from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
