from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from recipes.api.serializers import (
    CategorySerializer,
    IngredientSerializer,
    RecipeCrudSerializer,
    RecipeSerializer,
    RecipeIngredientMixSerializer,
    RecipeIngredientMixCrudSerializer,
)
from recipes.api.mixins import AdminOrReadOnlyMixin
from recipes.selectors.category import (
    get_public_categories,
    get_private_categories,
    get_public_categories_by_name,
)
from recipes.selectors.ingredient import get_all_ingredients
from recipes.selectors.recipes import get_all_recipes
from recipes.selectors.recipe_ingredient import get_all_recipe_ingredient_mix
from recipes.services.recipe_ingredient import create_many_recipe_ingredient_mix
from recipes.services.recipes import create_recipe
from .pagination import StandardResultsSetPagination

class CategoryViewSet(AdminOrReadOnlyMixin, ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            query_set = get_private_categories()
        else:
            query_set = get_public_categories()
        return query_set

    @action(detail=False, methods=["get"], name="Search Categories")
    def search(self, request):
        params = request.query_params.get("name")
        qs = get_public_categories_by_name(params)
        serializer = serializer = self.get_serializer(instance=qs, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class IngredientViewSet(AdminOrReadOnlyMixin, ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = get_all_ingredients()


class RecipeViewSet(ModelViewSet):
    queryset = get_all_recipes()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == "update":
            return RecipeCrudSerializer
        else:
            return RecipeSerializer

    def create(self, *arg, **kwargs):
        # Split request data and set variables
        data = self.request.data
        
        data["owner"] = self.request.user.id
        
        # Check and save ingredients 
        ingredients_mix_list = self.request.data.pop("ingredients_list")

        # Create Recipe instance
        recipe = create_recipe(data=data, SerializerClass=RecipeCrudSerializer)

        # Create ingredients.mix
        create_many_recipe_ingredient_mix(
            recipe, ingredients_mix_list, RecipeIngredientMixCrudSerializer
        )

        # Return Main serializer
        serializer = self.get_serializer(instance=recipe)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
    

    

class IngredientViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return RecipeIngredientMixSerializer
        else:
            return RecipeIngredientMixCrudSerializer

    queryset = get_all_recipe_ingredient_mix()