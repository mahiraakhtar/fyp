
from django.urls import path
from . import views

app_name='patientdetails'
urlpatterns = [

    path('patient/', views.IndexView.as_view(), name='patientindex'),
    path('patient/<pk>/', views.DetailView.as_view(), name='detail'),
    path('addpatient/', views.patientcreate.as_view(), name='patientcreate'),
    path('updatepatient/<pk>/', views.patientupdate.as_view(), name='patientupdate'),
	path('deletepatient/<pk>/', views.patientdelete.as_view(), name='patientdelete'),

]