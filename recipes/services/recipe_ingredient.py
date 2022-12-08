

def create_many_recipe_ingredient_mix(recipe, ingredients_list, SerializerClass):
    for recipe_mix in ingredients_list:
        recipe_mix['recipe'] = recipe.id
        recipe_mix_serializer = SerializerClass(data=recipe_mix)
        recipe_mix_serializer.is_valid(raise_exception=True)
        recipe_mix_serializer.save()