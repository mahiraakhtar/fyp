
from django.urls import path
from . import views

app_name='patientdetails'
urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.patientindex, name='patientindex'),
    path('patient/<pk>/', views.DetailView.as_view(), name='detail'),
    path('addpatient/', views.patientcreate.as_view(), name='patientcreate'),
]