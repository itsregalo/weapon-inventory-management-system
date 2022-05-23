from unicodedata import category
from django.shortcuts import render
from inventory.models import WeaponCategory, WeaponBrandSupplier, WeaponSubCategory

# Create your views here.

def IndexView(request):
    categories = WeaponCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'core/index.html', context)