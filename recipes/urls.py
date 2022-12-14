from django.urls import path, include

from recipes.api.router import router

urlpatterns = [
    path("rest/", include(router.urls)),

]
