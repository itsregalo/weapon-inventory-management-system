from django.contrib import admin
from .models import WeaponCategory, WeaponBrandSupplier, Weapon, WeaponAssigned
# Register your models here.


class WeaponBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(WeaponCategory, WeaponBrandAdmin)


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon_unique_id', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'weapon_unique_id')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Weapon, WeaponAdmin)

class WeaponAssignedAdmin(admin.ModelAdmin):
    list_display = ('user', 'weapon', 'assigned_time', 'date_returned')
    list_filter = ('assigned_time',)
    search_fields = ('user', 'weapon')

admin.site.register(WeaponAssigned, WeaponAssignedAdmin)