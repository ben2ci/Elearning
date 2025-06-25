from http import HTTPStatus
from django.http import HttpResponse
from django.shortcuts import render

from .models import Meal


# Create your views here.
def index(request):
    if request.method == 'GET':
        meals = Meal.objects.all()

        all_meals = {
            'meal_one': meals.filter(id=1).last(),
            'meal_two': meals.filter(id=2).last(),
            'meal_three': meals.filter(id=3).last(),
        }
        context = {
            'meals': all_meals,
        }

        return render(request, 'restaurant/index.html', context)
    return HttpResponse(status=HTTPStatus.BAD_REQUEST)
