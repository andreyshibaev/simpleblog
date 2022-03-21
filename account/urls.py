from django.urls import path
from . import views
from account.views import ChangePasswordView


app_name = 'account'

urlpatterns = [
    path('register/', views.register_account, name='signupuser'),
    path('login/', views.login_account, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/', views.profileuser, name='profileuser'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]