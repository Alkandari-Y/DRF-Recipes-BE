from recipes.models import Category

def get_private_categories():
    return Category.objects.all()

def get_public_categories():
    return Category.public.all_active()
