from django.db import models
from accounts.models import User
# Create your models here.

class WeaponBrand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=500)

    def no_of_weapons_in_category(self):
        return self.weapon_set.count()

    def __str__(self):
        return self.name

class WeaponBrandSupplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=500)

    def no_of_weapons_in_category(self):
        return self.weapon_set.count()

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    weapon_id = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(WeaponBrand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='weapons/', null=True, blank=True)
    quantity_available = models.IntegerField(default=0)
    in_inventory = models.BooleanField(default=True)

    # method to return the number of weapons in the database
    @staticmethod
    def get_count():
        return Weapon.objects.count()

    def __str__(self):
        return self.name