from rest_framework.viewsets import ModelViewSet

from recipes.serializers import CategorySerializer, IngredientSerializer
from recipes.selectors.category import get_public_categories, get_private_categories
from recipes.selectors.ingredient import get_all_ingredients
from recipes.mixins import AdminOrReadOnlyMixin

class CategoryViewSet(
    AdminOrReadOnlyMixin,
    ModelViewSet
    ):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            query_set = get_private_categories()
        else:
            query_set = get_public_categories()
        return query_set


class IngredientViewSet(
    AdminOrReadOnlyMixin,
    ModelViewSet
    ):
    serializer_class = IngredientSerializer
    queryset = get_all_ingredients()
