from unicodedata import category
from django.shortcuts import render
from inventory.models import WeaponCategory, WeaponBrandSupplier, WeaponSubCategory
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def IndexView(request):
    categories = WeaponCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'core/index.html', context)