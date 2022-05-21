from django.urls import path

from .views import index, add, update, show, delete

urlpatterns = [
    path('', index, name="index"),
    path('add/', add, name="add-todo"),
    path('show/<id>', show, name="show-todo"),
    path('edit/', update, name="edit-todo"),
    path('delete/<id>', delete, name="delete-todo"),
]
