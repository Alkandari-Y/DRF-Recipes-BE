from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from recipes.serializers import (
    CategorySerializer, 
    IngredientSerializer, 
    RecipeSerializer,
    RecipeIngredientMix
)
from recipes.mixins import AdminOrReadOnlyMixin
from recipes.selectors.category import (
    get_public_categories, 
    get_private_categories,
)
from recipes.selectors.ingredient import get_all_ingredients
from recipes.selectors.recipes import get_all_recipes

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

class RecipeViewSet(
    ModelViewSet
    ):
    serializer_class = RecipeSerializer
    queryset = get_all_recipes()

    def create(self, serializer):
        data = self.request.data
        data['owner']=self.request.user.id
        # data['ingredientset'] = []
        # for ingredient in data["ingredients_list"]:
        #     data['ingredientset'].append(ingredient)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
