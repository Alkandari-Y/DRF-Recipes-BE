from recipes.models import Category

def get_private_categories():
    return Category.objects.all()

def get_public_categories():
    return Category.public.all_active()


def get_public_categories_by_name(query):
    return Category.public.search(query=query)