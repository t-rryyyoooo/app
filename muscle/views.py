from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from collections import defaultdict
from . import PARTS

def recordIndexFunc(request):
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

def addMenuFunc(request):
    return HttpResponse("addMenu")
