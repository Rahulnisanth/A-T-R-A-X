from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *


def homePage(request):
    return render(request, "heroPage.html")


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects.html", context)


def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "single-project.html", context)


@login_required(login_url="loginUser")
def likeProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "GET" or request.method == "POST":
        user = request.user.profile
        if user not in project.like.all():
            project.like.add(user)
        else:
            project.like.remove(user)
        return redirect("projects")
    return render(request, "projects.html")


@login_required(login_url="loginUser")
def addProject(request):
    profile = request.user.profile
    project_form = ProjectForm(instance=profile)
    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Your new project is added successfully!")
            return redirect("projects")
    context = {"form": project_form}
    return render(request, "project-form.html", context)


def events(request):
    return render(request, "events.html")


def fosters(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "jobFosters.html", context)


@login_required(login_url="loginUser")
def addJob(request):
    profile = request.user.profile
    job_form = JobForm(instance=profile)
    if request.method == "POST":
        job_form = JobForm(request.POST, request.FILES)
        if job_form.is_valid():
            Job = job_form.save(commit=False)
            Job.owner = profile
            Job.save()
            return redirect("jobs")
    context = {"form": job_form}
    return render(request, "job-form.html", context)
