from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginUser, name="loginUser"),
    path("register-user/", views.registerUser, name="registerUser"),
    path("logout/", views.logoutUser, name="logoutUser"),
]
