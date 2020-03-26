from django.urls import path
from . import views
from calendars.views import AppointmentCreate

app_name = 'calendars'
urlpatterns = [
        path('', views.index, name='index'),
        path('appointment/', AppointmentCreate.as_view(), name='appointment-add'),
        path('<int:calendar_id>/', views.detail, name='detail'),
        ]
