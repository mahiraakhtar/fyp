
from django.urls import path
from . import views

app_name='patientdetails'
urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.patientindex, name='patientindex'),
]