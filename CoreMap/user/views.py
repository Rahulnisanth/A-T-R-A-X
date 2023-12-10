from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm


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
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password, Please try again!")
    context = {"flag": flag}
    return render(request, "authentication.html", context)


def logoutUser(request):
    logout(request)
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
