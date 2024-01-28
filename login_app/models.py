from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): # This means that the User class includes all the fields and methods provided by AbstractUser and can be customized further.
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,unique = True)
    password = models.CharField(max_length = 255)
    username = None
    USERNAME_FIELD = 'email' # since abstract user needs username to and pass to login but we need email and pass 
    REQUIRED_FIELDS =[]
