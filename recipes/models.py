from django.db import models
from django.contrib.auth import get_user_model

from recipes.managers import CategoryManager

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=False)
    public = CategoryManager()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ("name",)


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    description = models.CharField(max_length=250)
    steps = models.TextField(default="", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredientMix",
        through_fields=("recipe", "ingredient"),
    )

    def __str__(self) -> str:
        return self.name


class RecipeIngredientMix(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredient_mix_set"
    )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe_mix_set"
    )
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.recipe.name}: {self.ingredient.name}"


class ModelImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()
