from rest_framework import serializers

from recipes.models import (
    Category, 
    Ingredient, 
    RecipeIngredientMix, 
    Recipe,
)
from recipes.validators import (
    unique_ingredient_name, 
    unique_category_name,
)

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[unique_category_name])
    status = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField(write_only=True, default=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'status', 'active']
    
    def get_status(self, obj):
        property_status = {
            'active': obj.active
        }
        if not obj.active:
            property_status['message'] = 'Pending approval'
        return property_status


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[unique_ingredient_name])
    class Meta:
        model = Ingredient
        fields = ['id', 'name']



class RecipeIngredientMixSerializer(serializers.ModelSerializer):    
    class Meta:
        model = RecipeIngredientMix
        fields = ['id', 'ingredient', 'amount', 'unit']


class RecipeIngredientMixCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredientMix
        fields = ['id', 'ingredient', 'recipe', 'amount', 'unit']

class RecipeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "description",
            "steps",
            "date_created",
            "date_modified",
            "category",
            "owner",
        ]

class RecipeSerializer(RecipeBaseSerializer):
    ingredients_list = RecipeIngredientMixSerializer(source='ingredientset', many=True)
    class Meta(RecipeBaseSerializer.Meta):
        fields = [
            "ingredients_list",
            *RecipeBaseSerializer.Meta.fields
        ]
    
    def update(self, instance, validated_data):
        print(validated_data)
        return validated_data