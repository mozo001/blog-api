
from django.urls import path
from .views import (
    api_blog_list, 
    api_blog_create, 
    api_blog_detail, 
    api_blog_change,
    api_blog_update, 
    api_blog_delete,
    blog_list,
    blog_create,
    blog_detail,
    blog_update,
    blog_delete,
)

urlpatterns = [
    # DRF API Urls
    path('blogs/', api_blog_list, name='blog-list'),
    path('blogs/create/', api_blog_create, name='blog-create'),
    path('blogs/<uuid:pk>/', api_blog_detail, name='blog-detail'),
    path('blogs/<uuid:pk>/update/', api_blog_update, name='blog-update'),
    path('blogs/<uuid:pk>/update/', api_blog_change, name='blog-update'),
    path('blogs/<uuid:pk>/delete/', api_blog_delete, name='blog-delete'),

    #HTML Templates Urls
    path("", blog_list, name="blog_list"),
    path("create/",blog_create, name="blog_create"),
    path("<uuid:pk>/", blog_detail, name="blog_detail"),
    path("<uuid:pk>/update/", blog_update, name="blog_update"),
    path("<uuid:pk>/delete/", blog_delete, name="blog_delete"),
    
  
]



