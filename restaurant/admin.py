from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available', 'image')

    search_fields = ('name', 'description')


# Register your models here.
# admin.site.register(Meal, MealAdmin)
