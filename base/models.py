from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True)
    phone_number = models.CharField(max_length = 200, null = True)
    admin = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.first_name 

    # admins get moved up to top of the list
    class Meta:
        ordering = ['-admin']