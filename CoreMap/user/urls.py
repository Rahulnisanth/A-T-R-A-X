from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginUser, name="loginUser"),
    path("register-user/", views.registerUser, name="registerUser"),
    path("logout/", views.logoutUser, name="logoutUser"),
    # Profile alterations [C R U D]:
    path("user-profile/", views.userProfile, name="user-profile"),
    path("edit-profile/", views.editProfile, name="edit-profile"),
    # Profiles Dirs:
    path("profiles-cse/", views.CSEProfiles, name="profiles-cse"),
]
