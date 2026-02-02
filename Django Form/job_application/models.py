from django.db import models

# 1st step
# Create your models here.

class Form(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
