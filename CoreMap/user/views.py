from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
def LoginUser(request):
    flag = "login"
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Atrax welcomes you {username} !")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password, Please try again!")
    context = {"flag": flag}
    return render(request, "authentication.html", context)


@login_required(login_url="loginUser")
def logoutUser(request):
    logout(request)
    messages.error(request, "User have logged out from Atrax !")
    return redirect("/")


def registerUser(request):
    flag = "register"
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(
                request,
                f"Hello {user.username}!,Your account has been registered successfully!",
            )
            login(request, user)
            return redirect("/")
    context = {"flag": flag, "form": form}
    return render(request, "authentication.html", context)


@login_required(login_url="loginUser")
def userProfile(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "user-profile.html", context)


@login_required(login_url="loginUser")
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated successfully")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "profile-form.html", context)


def CSEProfiles(request):
    targeted_departments = ["CSE", "Computer Science Engineering", "Computer Science"]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-cse.html", context)


def ECEProfiles(request):
    targeted_departments = [
        "ECE",
        "Electronics and Communication Engineering",
        "Electronics and Communication ",
    ]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-ece.html", context)


def ITProfiles(request):
    targeted_departments = ["IT", "Information Technology"]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-it.html", context)


def AIDSProfiles(request):
    targeted_departments = ["AIDS", "Artificial Intelligence and Data Science"]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-aids.html", context)


def AIMLProfiles(request):
    targeted_departments = ["AIML", "Artificial Intelligence and Machine Learning"]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-aiml.html", context)


def CSProfiles(request):
    targeted_departments = ["CS", "Cybersecurity", "Cyber"]
    profiles = Profile.objects.filter(department__in=targeted_departments)
    context = {"profiles": profiles}
    return render(request, "profiles-cs.html", context)


@login_required(login_url="loginUser")
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "New Skill has been added successfully")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "skill-form.html", context)


@login_required(login_url="loginUser")
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully edited {skill.name}")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "skill-form.html", context)


def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.error(request, f"{skill.name} has been deleted!")
        return redirect("user-profile")
    context = {"skill": skill}
    return render(request, "delete-skill.html", context)


@login_required(login_url="loginUser")
def userProjects(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "user-projects.html", context)
