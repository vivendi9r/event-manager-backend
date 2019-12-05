from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Owner(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return (str)(self.user)

class Event(models.Model):
    name = models.CharField(max_length=200)
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    client = models.ManyToManyField(User)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

