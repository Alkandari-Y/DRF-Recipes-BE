def create_recipe(data, SerializerClass):
        recipe_serializer = SerializerClass(data=data)
        recipe_serializer.is_valid(raise_exception=True)
        recipe = recipe_serializer.save()
        return recipe