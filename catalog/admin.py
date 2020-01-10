from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import QUser, Book, UserProfile

admin.site.register(QUser)
admin.site.register(UserProfile)
admin.site.register(Book)
