from django.urls import path
from .views import index, CreatePost, DeletePost,DetailPost,UpdatePost, get_countries_by_name


urlpatterns = [
    path('blog-index/', index, name='blog_index'),
    path('create-post/',CreatePost.as_view(), name='create_post'),
    path('delete-post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('detail-post/<int:pk>/', DetailPost, name='detail_post'),
    path('update-post/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    # path('countries/<str:country_name>/', get_countries_by_name),
]
