from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # This is a model class to add an additional information that the default user(that we import above) does not have.Default user already have things like username, password, firstname, lastname, email 
    # user wrtten below is an attribute
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)

    # additional atrributes
    # blank=True means that the user doesn't have to fill it out i.e. optional. 
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username