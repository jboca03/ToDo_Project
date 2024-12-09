from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin', default=False)
    is_user = models.BooleanField('Is Regular User', default=True)

    def __str__(self):
        return self.username

# Task model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
