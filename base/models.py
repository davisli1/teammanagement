import email
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    number = models.CharField(max_length = 200, null = True)
    admin = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.first_name or ''

    # when complete it is sent to the bottom
    class Meta:
        ordering = ['-admin']
