from django.db import models
# abstract base class
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.text import slugify

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

class Soldier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
