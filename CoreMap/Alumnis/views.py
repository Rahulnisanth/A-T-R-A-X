from django.shortcuts import render


def homePage(request):
    return render(request, "heroPage.html")


def projects(request):
    return render(request, "projects.html")


def events(request):
    return render(request, "events.html")


def fosters(request):
    return render(request, "jobFosters.html")
