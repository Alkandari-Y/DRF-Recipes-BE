from recipes.models import Ingredient


def get_all_ingredients():
    return Ingredient.objects.all()
