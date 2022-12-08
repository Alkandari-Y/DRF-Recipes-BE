from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from recipes.serializers import (
    CategorySerializer, 
    IngredientSerializer,
    RecipeBaseSerializer,
    RecipeIngredientMixCreateSerializer,
    RecipeSerializer,
)
from recipes.mixins import AdminOrReadOnlyMixin
from recipes.selectors.category import (
    get_public_categories, 
    get_private_categories,
    get_public_categories_by_name,
)
from recipes.selectors.ingredient import get_all_ingredients
from recipes.selectors.recipes import get_all_recipes
from recipes.services.recipe_ingredient import create_many_recipe_ingredient_mix
from recipes.services.recipes import create_recipe
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
    
    @action(detail=False, methods=['get'], name='Search Categories')
    def search(self, request):
        params = request.query_params.get("name")
        qs = get_public_categories_by_name(params)
        serializer = serializer = self.get_serializer(instance=qs, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, *arg, **kwargs):
        # Split request data and set variables
        data = self.request.data
        ingredients_mix_list = self.request.data.pop('ingredients_list')
        data['owner']=self.request.user.id

        # Create Recipe instance
        recipe = create_recipe(
            data=data,
            SerializerClass=RecipeBaseSerializer
        )

        # Create ingredients.mix
        create_many_recipe_ingredient_mix(
            recipe, 
            ingredients_mix_list, 
            RecipeIngredientMixCreateSerializer
        )

        # Return Main serializer
        serializer = self.get_serializer(instance=recipe)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

