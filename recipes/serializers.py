from rest_framework import serializers

from recipes.models import Category, Ingredient, RecipeIngredientMix
from recipes.validators import unique_ingredient_name, unique_category_name
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
    