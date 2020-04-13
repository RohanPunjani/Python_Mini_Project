from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit_blog, name='edit_blog'),
    path('create/<str:heading>', views.create_blog, name='create_blog'),
    path('delete/<int:id>', views.delete_blog, name='delete_blog'),
    path('edit/publish/<int:id>', views.publish_blog, name='publish_blog'),
]
