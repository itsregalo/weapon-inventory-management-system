from .models import WeaponCategory, WeaponBrandSupplier, WeaponSubCategory, Weapon
from django.shortcuts import render

def WeaponCategoryDetail(request, slug):
    category = WeaponCategory.objects.get(slug=slug)
    weapons = Weapon.objects.filter(category=category)
    context = {
        'category': category,
        'weapons': weapons
    }
    return render(request, 'core/weapon_cat_detail.html', context)