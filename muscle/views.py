from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Part, Menu, Record
from collections import defaultdict
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import AddMenuForm, AddRecordForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models.query import QuerySet

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
    for part in parts:
        obj = Menu.objects.filter(part = part)
        objects.append({"part" : part, "menus" : obj})

    #objects = Menu.objects.all().order_by("part")

    contexts = {
            "objects" : objects, 
            "valid" : valid
            }
    

    return render(request, "recordIndex.html", contexts)

def listFunc(request):
    """
    query = Record.objects.all().query
    query.group_by = ["date"]
    records = QuerySet(query=query, model=Record).order_by("date").reverse()
    """
    records = Record.objects.all().order_by("date", "menu").reverse()

    contexts = {
            "records" : records}
    return render(request, "recordList.html", contexts)

@login_required()
def recordDetailFunc(request, menu_pk):
    form = AddRecordForm(request.POST or None)
    print(form)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("recordList")

    parts = Part.objects.all()
    menu = Menu.objects.get(pk=menu_pk)
    part = Part.objects.get(pk=menu.part.pk)
    created_on = timezone.now()

    contexts = {
            "parts" : parts, 
            "part" : part, 
            "menu" : menu, 
            "created_on" : created_on 

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
def menuEditFunc(request, pk):
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
    return render(request, "menuEdit.html", contexts)

@login_required()
def recordEditFunc(request, pk):
    record = get_object_or_404(Record, pk=pk)
    form = AddRecordForm(request.POST or None, instance=record)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("recordList")

    obj = Record.objects.get(pk=pk)

    contexts = {
            "object" : obj, 
            "pk" : pk,
            }
    return render(request, "recordEdit.html", contexts)

def recordDeleteFunc(request, pk):
    obj = Record.objects.get(pk=pk)
    obj.delete()
    return redirect("recordList")

def menuDeleteFunc(request, pk):
    obj = Menu.objects.get(pk=pk)
    obj.delete()
    return redirect("recordIndex")

