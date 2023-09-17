from django.db import models
from User.models import User


class Teacher(User):
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Room(models.Model):
    RoomID = models.BigAutoField(primary_key=True)
    RoomName = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.RoomID) + " " + str(self.RoomName)


class Event(models.Model):
    EventID = models.AutoField(primary_key=True)
    EventTitle = models.CharField(max_length=100, null=False)
    DateofEvent = models.DateTimeField()
    MaxParticipants = models.IntegerField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.EventTitle


class Specialization(models.Model):
    teacher = models.ForeignKey('Teacher.Teacher',  on_delete=models.CASCADE, related_name='teacher_specialize') # Use a string to avoid direct import
    specialization = models.CharField(max_length=100, null=False)