from django.db import models
# abstract base class
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

# users class
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_soldier = models.BooleanField(default=False)


    # __str__ method to return the username of the user
    def __str__(self):
        return self.username


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
