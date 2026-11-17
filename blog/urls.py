
from django.urls import path
from .views import (
    blog_list, 
    blog_create, 
    blog_detail, 
    blog_update, 
    
    blog_delete
)

urlpatterns = [
    path('', blog_list, name='blog-list'),
    path('blogs/create/', blog_create, name='blog-create'),
    path('blogs/<uuid:pk>/', blog_detail, name='blog-detail'),
    path('blogs/<uuid:pk>/update/', blog_update, name='blog-update'),
    path('blogs/<uuid:pk>/delete/', blog_delete, name='blog-delete'),
  
]



