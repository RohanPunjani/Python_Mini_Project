from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit_blog, name='edit_blog'),
    path('create/<str:heading>', views.create_blog, name='create_blog'),
    path('create/block/<int:id>/<str:title>/<str:content>',
         views.create_block, name='create_block'),
    path('update/<int:blogId>/block/<int:id>/<str:isMerged>',
         views.update_block, name='update_block'),
    path('update/<int:blogId>/block/<int:id>/<str:title>/<str:content>',
         views.update_block_content, name='update_block_content'),
    path('delete/<int:id>', views.delete_blog, name='delete_blog'),
    path('delete/<int:id>/block/<int:blockid>',
         views.delete_block, name='delete_block'),
    path('edit/publish/<int:id>', views.publish_blog, name='publish_blog'),
]
