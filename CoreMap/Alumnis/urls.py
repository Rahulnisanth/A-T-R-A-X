from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    # Projects Section:
    path("projects/", views.projects, name="projects"),
    path("add-project/", views.addProject, name="add-project"),
    path("like-project/", views.likeProject, name="like-project"),
    # Events Section:
    path("events/", views.events, name="events"),
    # Job openings Section:
    path("Job-Fosters/", views.fosters, name="JobFosters"),
    path("add-job/", views.addJob, name="add-job"),
]
