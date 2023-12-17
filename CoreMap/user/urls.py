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
    path("profiles-ece/", views.ECEProfiles, name="profiles-ece"),
    path("profiles-it/", views.ITProfiles, name="profiles-it"),
    path("profiles-aids/", views.AIDSProfiles, name="profiles-aids"),
    path("profiles-cs/", views.CSProfiles, name="profiles-cs"),
    path("profiles-aiml/", views.AIMLProfiles, name="profiles-aiml"),
]
