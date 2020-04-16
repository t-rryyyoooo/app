from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("recordIndex/", recordIndexFunc, name="recordIndex"), 
        path("recordDetail/", recordDetailFunc, name="recordDetail"),
        path("addMenu/", addMenuFunc, name="addMenu"),
        path("login/", loginFunc, name="login")
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
