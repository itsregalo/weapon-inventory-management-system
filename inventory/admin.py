from django.contrib import admin
from .models import WeaponCategory, WeaponBrandSupplier, Weapon
# Register your models here.


class WeaponBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(WeaponCategory, WeaponBrandAdmin)


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('brand', 'category')
    search_fields = ('name', 'weapon_id')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Weapon, WeaponAdmin)