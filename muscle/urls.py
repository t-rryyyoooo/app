from django.urls import path
from .views import recordIndexFunc, addMenuFunc, recordDetailFunc

urlpatterns = [
        path("recordIndex", recordIndexFunc, name="recordIndex"), 
        path("recordDetail", recordDetailFunc, name="recordDetail"),
        path("addMenu", addMenuFunc, name="addMenu")
        ]
