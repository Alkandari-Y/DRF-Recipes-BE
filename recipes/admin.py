from django.contrib import admin
from .models import Category, Recipe, RecipeIngredientMix, Ingredient

admin.site.register([Category, Recipe, RecipeIngredientMix, Ingredient])
