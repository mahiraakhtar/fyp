
from django.urls import path
from . import views


app_name='patientdetails'
urlpatterns = [

    path('patient/', views.patientindex.as_view(), name='patientindex'),
    path('patient/<pk>/', views.patientdetail.as_view(), name='patientdetail'),
    path('addpatient/', views.patientcreate.as_view(), name='patientcreate'),
    path('patientupdate/<pk>/', views.patientupdate.as_view(), name='patientupdate'),
    path('deletepatient/<pk>/', views.patientdelete.as_view(), name='patientdelete'),
    path('addtest/<patient_id>/', views.testcreate, name='testcreate'),
    path('inferform/', views.inferform, name='inferform'),
    path('infer/', views.infer, name='infer'),
    path('<patient_id>/deletetest/<testresult_id>/', views.testdelete, name='testdelete'),

	path('insertsymplist/', views.symplist, name='insertsymplist'),
	path('addtest/', views.addtest.as_view(), name='addtest'),
	path('deletetest/<pk>/', views.deletetest.as_view(), name='deletetest'),
	path('updatetest/<pk>/', views.updatetest.as_view(), name='updatetest'),
	path('indextest/', views.testindex.as_view(), name='testindex'),

]