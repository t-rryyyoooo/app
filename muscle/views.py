from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Part, Menu
from collections import defaultdict
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import AddMenuForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def recordIndexFunc(request):
    form = AddMenuForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("recordIndex")

    objects = []
    parts = Part.objects.all()
    for i, part in enumerate(parts):
        obj = Menu.objects.filter(part = part)
        objects.append({"part" : part, "menus" : obj, "i" : i + 1 })

    contexts = {
            "objects" : objects, 
            }

    return render(request, "recordIndex.html", contexts)

def recordDetailFunc(request, part):
    objects = Menu.objects.get(part=part)

    return render(request, "recordDetail.html", {"objects" : objects})

def loginFunc(request):
    if request.method == "POST":
        postedUserName = request.POST["username"]
        postedPassword = request.POST["password"]
        user = authenticate(request, username = postedUserName, password = postedPassword)
        if user is not None:
            login(request, user)
            return redirect("recordIndex")

    return render(request, "login.html")

def logoutFunc(request):
    logout(request)
    return redirect("recordIndex")

@login_required()
def editFunc(request, pk):
    menu = get_object_or_404(Menu, pk = pk)
    form = AddMenuForm(request.POST or None, instance=menu)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("recordIndex")

    parts = Part.objects.all()
    obj = Menu.objects.get(pk = pk)

    context = {
            "object" : obj, 
            "pk" : pk,
            "parts" : parts
            }
    return render(request, "edit.html", context)


def deleteFunc(request, pk):
    obj = Menu.objects.get(pk = pk)
    obj.delete()
    return redirect("recordIndex")

