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


class RecipeSerializer(serializers.ModelSerializer):
    ingredients_list = RecipeIngredientMixSerializer(source='ingredientset', many=True)
    class Meta:
        model = Recipe
        fields = [
            "id",
            "ingredients_list",
            "name",
            "description",
            "steps",
            "date_created",
            "date_modified",
            "category",
            "owner",
        ]

    def create(self, validated_data):
        ingredient_mix = validated_data.pop('ingredientset')
        print(dir(ingredient_mix))
        print(validated_data)
        recipe = Recipe.objects.create(**validated_data)
        for ing in ingredient_mix:
            new_mix_obj = RecipeIngredientMix.objects.create(recipe=recipe, **ing)
            print(new_mix_obj)
            mix_serializer = RecipeIngredientMixSerializer(data=new_mix_obj)
            print('pre valid')
            mix_serializer.is_valid(raise_exception=True) # serializer results in failure
            print('post valid')

            obj = mix_serializer.save()
            print(obj)
            validated_data['ingredientset'] = obj
        return validated_data