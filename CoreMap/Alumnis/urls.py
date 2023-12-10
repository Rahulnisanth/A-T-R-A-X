from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("projects/", views.projects, name="projects"),
    path("events/", views.events, name="events"),
    path("Job-Fosters/", views.fosters, name="JobFosters"),
]
