from django.urls import path, include

from recipes import views

urlpatterns = [
    path('', views.get_index, name='index'),

]
