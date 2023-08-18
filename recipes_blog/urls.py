from django.urls import path
from .views import index, CreatePost


urlpatterns = [
    path('blog-index/', index, name='blog_index'),
    path('create-post/',CreatePost.as_view(), name='create_post'),
]
