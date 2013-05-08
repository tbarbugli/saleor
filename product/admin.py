from django.contrib import admin
# from .models import DigitalShip, Ship, Category
from .models import Category
from mptt.admin import MPTTModelAdmin

# admin.site.register(DigitalShip)
# admin.site.register(Ship)
admin.site.register(Category, MPTTModelAdmin)
