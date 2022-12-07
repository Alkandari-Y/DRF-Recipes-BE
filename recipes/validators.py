
from rest_framework.validators import UniqueValidator

from recipes.selectors.category import get_private_categories
from recipes.selectors.ingredient import get_all_ingredients

unique_category_name = UniqueValidator(queryset=get_private_categories(), lookup='iexact')

unique_ingredient_name = UniqueValidator(queryset=get_all_ingredients(), lookup='iexact')