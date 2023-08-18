from django.urls import path
from .views import index, CreatePost, DeletePost,DetailPost


urlpatterns = [
    path('blog-index/', index, name='blog_index'),
    path('create-post/',CreatePost.as_view(), name='create_post'),
    path('delete-post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('detail-post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
]
