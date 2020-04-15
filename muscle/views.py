from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Menu
from collections import defaultdict
from . import PARTS
from .forms import AddMenuForm

def recordIndexFunc(request):
    print(request.method)
    form = AddMenuForm(request.POST or None)
    print(form)
    if request.method == "POST" and form.is_valid():
        form.save()
        print(form)
        print("OK")
        return redirect("recordIndex")

    print("NO")
    objects = {}
    for part in PARTS:
        objects[part] = Menu.objects.filter(part = part)

    contexts = {
            "objects" : objects
            }

    return render(request, "recordIndex.html", contexts)

def recordDetailFunc(request, part):
    objects = Menu.objects.get(part=part)

    return render(request, "recordDetail.html", {"objects" : objects})

def addMenuFunc(request, part = None):

    contexts = {
            "form" : AddMenuForm(), 
            "part" : part
            }
    return render(request, "addMenu.html", contexts)
