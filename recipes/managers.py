from django.db import models
from django.db.models import Q

class CategoryQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(active=True) | Q(name__icontains=query)
        return self.filter(lookups)

    def all_active(self):
        return self.filter(active=True)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)
    def all_active(self):
        return self.get_queryset().all_active()
