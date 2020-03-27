from django.urls import path
from . import views

app_name = 'calendars'
urlpatterns = [
        path('', views.appointment_list, name='appointment_list'),
        path('appointment/', views.create_appointment, name='create_appointment'),
        path('<int:appointment_id>/', views.details, name='details'),
        ]
