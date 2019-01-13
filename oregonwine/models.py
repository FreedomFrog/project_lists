from django.db import models

# Create your models here.
class Winery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    ava = models.ForeignKey('AVA', on_delete=models.CASCADE,)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    websitelink = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AVA(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

