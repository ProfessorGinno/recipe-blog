from django.urls import path
from .views import index

urlpatterns = [
    path('blog-index/', index, name='blog_index'),
]
