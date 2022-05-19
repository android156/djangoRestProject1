from django.contrib import admin

# Register your models here.
from userapp.models import AppUser

admin.site.register(AppUser)
