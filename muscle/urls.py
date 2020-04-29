from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("", recordIndexFunc, name="recordIndex"), 
        path("recordList", listFunc, name="recordList"), 
        path("recordListPerMenu", recordListPerMenuFunc, name="recordListPerMenu"), 
        path("recordDetail/<int:menu_pk>/", recordDetailFunc, name="recordDetail"),
        path("login/", loginFunc, name="login"),
        path("logout/", logoutFunc, name="logout"), 
        path("menuEdit/<int:pk>/",menuEditFunc, name="menuEdit"),
        path("recordEdit/<int:pk>/",recordEditFunc, name="recordEdit"),
        path("recordDetailFromCalendar/<int:year>/<int:month>/<int:day>/",recordDetailFromCalendarFunc, name="recordDetailFromCalendar"),
        path("menuDelete/<int:pk>/",menuDeleteFunc , name="menuDelete"),
        path("recordDelete/<int:pk>/",recordDeleteFunc , name="recordDelete") , 
        path("calendar/", MonthCalender.as_view(), name="calendar"),
        path("calendar/<int:year>/<int:month>/", MonthCalender.as_view(), name="calendar")
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
