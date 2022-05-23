from tabnanny import verbose
from unicodedata import category
from django.db import models
from accounts.models import User
from django.utils.text import slugify
# Create your models here.

class WeaponCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    fa_object = models.CharField(max_length=50, blank=True, null=True)

    def no_of_weapons_in_category(self):
        return self.weapon_set.count()

    class Meta:
        verbose_name_plural = 'Weapon Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name+'-'+str(self.id))
        if not self.fa_object:
            self.fa_object = 'green'
        return super(WeaponCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class WeaponBrandSupplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(WeaponCategory, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(max_length=500)

    # method to create a slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def no_of_weapons_in_category(self):
        return self.weapon_set.count()

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    weapon_unique_id = models.CharField(max_length=50, blank=True, unique=True)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(WeaponCategory, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='weapons/', null=True, blank=True)
    quantity_available = models.IntegerField(default=0)
    in_inventory = models.BooleanField(default=True)

    # method to return the number of weapons in the database
    @staticmethod
    def get_count():
        return Weapon.objects.count()

    # method to add weapon_id 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name+'-'+str(self.id))
        if not self.weapon_id:
            self.weapon_id = '#'+self.slug
        return super(Weapon, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class WeaponAssigned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    weapon_name = models.CharField(max_length=50, blank=True, null=True)
    weapon_unque_id = models.CharField(max_length=50, blank=True, unique=True)
    assigned_time = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey(User, related_name='assigned_by', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_to', on_delete=models.CASCADE) 
    slug = models.SlugField(blank=True, null=True)
    was_returned = models.BooleanField(default=False, blank=True, null=True)
    date_returned = models.DateTimeField(blank=True, null=True)
    was_destroyed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'weapons assigned'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username+'-'+str(self.id))
        return super(WeaponAssigned, self).save(*args, **kwargs)
