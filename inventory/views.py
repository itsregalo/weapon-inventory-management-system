
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render

@login_required
def WeaponCategoryDetail(request, slug):
    category = WeaponCategory.objects.get(slug=slug)
    weapons = Weapon.objects.filter(category=category)
    weapons_assigned = WeaponAssigned.objects.filter(weapon__category=category)
    context = {
        'category': category,
        'weapons': weapons,
        'weapons_assigned': weapons_assigned,
    }
    return render(request, 'core/weapon_cat_detail.html', context)

@login_required
def WeaponList(request):
    weapons = Weapon.objects.all()
    context = {
        'weapons': weapons,
    }
    return render(request, 'core/weapons.html', context)