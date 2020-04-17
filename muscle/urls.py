from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("recordIndex/", recordIndexFunc, name="recordIndex"), 
        path("recordDetail/", recordDetailFunc, name="recordDetail"),
        path("login/", loginFunc, name="login"),
        path("logout/", logoutFunc, name="logout"), 
        path("edit/<int:pk>/",editFunc, name="edit"),
        path("delete/<int:pk>/",deleteFunc , name="delete") 
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
