from django.urls import path
from .views import homepage, about_us

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about_us, name='about')
]
