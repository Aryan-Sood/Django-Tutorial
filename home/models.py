from django.db import models

class Student(models.Model):
    id: models.AutoField
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Car(models.Model):
    car_name = models.CharField(max_length=40)
    speed = models.IntegerField(default=50)