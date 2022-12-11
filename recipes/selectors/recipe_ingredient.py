from recipes.models import RecipeIngredientMix

def get_all_recipe_ingredient_mix():
    return RecipeIngredientMix.objects.all()