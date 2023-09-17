from django.db import models
from User.models import User


class Student(User):
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Attends(models.Model):
    username = models.ForeignKey('Student.Student',  on_delete=models.CASCADE) # Use a string to avoid direct import
    eventid = models.ForeignKey('Teacher.Event', on_delete=models.CASCADE) # Use a string to avoid direct import
    status = models.IntegerField(default=0)
    dateRegistered = models.DateTimeField()

    def __str__(self):
        return f"{self.username.username} - {self.eventid.EventTitle}"
