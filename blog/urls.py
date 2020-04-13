from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit_blog, name='edit_blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('delete/<int:id>', views.delete_blog, name='delete_blog'),
]
