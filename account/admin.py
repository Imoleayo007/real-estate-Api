from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

# Register your models here.

admin.site.register(User)
