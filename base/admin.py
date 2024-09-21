from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Subject, Subtopic


# UserAdmin class having all the necessary configuration for admin panel
# User class which inherits properties and fields etc from AbstractUser


admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Subtopic)

