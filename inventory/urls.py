from django.urls import path
from .views import *

app_name = 'inventory'

urlpatterns = [
    path('weapon/<slug:slug>/', WeaponCategoryDetail, name='weapon-detail'),
]
