from django.db import models

# Create your models here.


class Destination(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.IntegerField()
    picture= models.ImageField(upload_to="media/", null=True)

class Teams(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    picture= models.ImageField(upload_to="media/", null=True)
