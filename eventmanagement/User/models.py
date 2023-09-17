from django.db import models


# Create your models here.
class User(models.Model):
    Type = (('S', 'Student'), ('T', 'Teacher'))
    username = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=20, null=False)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=1, choices=Type, default='S')

    class Meta:
        abstract = True

