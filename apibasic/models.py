from django.db import models

# Create your models here.

class kraska(models.Model):
    name=models.CharField(max_length=100)
    karobka=models.CharField(max_length=100)
    soni=models.CharField(max_length=100)
    narxi=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
