from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# A Custom User class that inherits properties and fields from AbstractUser class.
# it is used to extend default User class with extra fields
# following_users is having many to many relation with User class
# AUTH_USER_MODEL is same as django's default User Class
class User(AbstractUser):
    following_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

# Subject table, with each row unique to a user
class Subject(models.Model):
    title = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # A string representaion of object (Subject)
    def __str__(self):
        return f'Subject: {self.title}'


# subtopic table, with each row unique to a user
class Subtopic(models.Model):
    title = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Subtopic: {self.title}'

# Quesion table
class Question(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    answer = models.TextField()

  
    def __str__(self):
        return f'Question: {self.title}'
