from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=50)
    phone_Number = models.CharField(max_length=16,unique=True)
    date_of_meeting = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Habits(models.Model):
    name = models.CharField(max_length=30)
    done_For_Today = models.CharField(max_length=200)
    important = models.CharField(max_length=150)
    comment = models.CharField(max_length=300)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)