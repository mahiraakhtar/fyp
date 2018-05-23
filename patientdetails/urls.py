
from django.urls import path
from . import views


app_name='patientdetails'
urlpatterns = [

    path('patient/', views.patientindex.as_view(), name='patientindex'),
    path('patient/<pk>/', views.patientdetail.as_view(), name='patientdetail'),
    path('addpatient/', views.patientcreate.as_view(), name='patientcreate'),
    path('addtest/<patient_id>/', views.testcreate, name='testcreate'),
    path('inferform/', views.inferform, name='inferform'),
    path('infer/', views.infer, name='infer'),
    path('<patient_id>/deletetest/<testresult_id>/', views.testdelete, name='testdelete'),
    path('updatepatient/<pk>/', views.patientupdate.as_view(), name='patientupdate'),
	path('deletepatient/<pk>/', views.patientdelete.as_view(), name='patientdelete'),
	path('insertsymplist/', views.symplist, name='insertsymplist'),

]