from django.contrib import admin
from passwordpractice.models import UserProfileInfo
# Register your models here.
# whenever we make changes in admin.py file always run the 'python manage.py migrate' command and 'python manage.pe makemigrations app_name'
admin.site.register(UserProfileInfo)
