from django.urls import path
from .views import UserLogin, UserSignUp, sign_up_success, UserLogout, profile, user_update, ChangePassword

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('sign-up-success/', sign_up_success, name='sign_up_success'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', user_update, name='update_user'),
    path('profile/change-password/', ChangePassword.as_view(), name='change_password'),
]
