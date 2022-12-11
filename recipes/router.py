from rest_framework import routers

from recipes import views

router = routers.SimpleRouter()
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"ingredients", views.IngredientViewSet)
router.register(r"recipes", views.RecipeViewSet)
router.register(r'recipes/ingredients/', views.IngredientViewSet)