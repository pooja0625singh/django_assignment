from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('completed/<list_id>', views.completed, name="completed"),
    path('edit/<list_id>', views.edit, name="edit"),
]
