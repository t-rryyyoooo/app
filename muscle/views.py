from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Part, Menu
from collections import defaultdict
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import AddMenuForm, AddRecordForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def recordIndexFunc(request):
    form = AddMenuForm(request.POST or None)
    valid = True
    if request.method == "POST": 
        if form.is_valid():
            form.save()
            return redirect("recordIndex")
        else:
            valid = False 

    objects = []
    parts = Part.objects.all()
    for i, part in enumerate(parts):
        obj = Menu.objects.filter(part = part)
        objects.append({"part" : part, "menus" : obj})

    contexts = {
            "objects" : objects, 
            "valid" : valid
            }

    return render(request, "recordIndex.html", contexts)

def listFunc(request):
    return HttpResponse("Hello")

def recordDetailFunc(request, part_pk , menu_pk):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("list")

    part = Menu.objects.get(pk=part_pk)
    menu = Menu.objects.get(pk=menu_pk)

    contexts = {
            "part" : part, 
            "menu" : menu
            }

    return render(request, "recordDetail.html", contexts)

def loginFunc(request):
    if request.method == "POST":
        postedUserName = request.POST["username"]
        postedPassword = request.POST["password"]
        user = authenticate(request, username=postedUserName, password=postedPassword)
        if user is not None:
            login(request, user)
            return redirect("recordIndex")

    return render(request, "login.html")

def logoutFunc(request):
    logout(request)
    return redirect("recordIndex")

@login_required()
def editFunc(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    form = AddMenuForm(request.POST or None, instance=menu)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("recordIndex")

    parts = Part.objects.all()
    obj = Menu.objects.get(pk=pk)

    contexts = {
            "object" : obj, 
            "pk" : pk,
            "parts" : parts
            }
    return render(request, "edit.html", contexts)


def deleteFunc(request, pk):
    obj = Menu.objects.get(pk=pk)
    obj.delete()
    return redirect("recordIndex")

