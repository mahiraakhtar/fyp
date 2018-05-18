
from django.urls import path
from . import views
app_name='nlp'
urlpatterns = [

    path('insert/', views.insertdatabase, name='insertdatabase'),
    path('diseases',views.IndexView.as_view(),name='diseaseindex'),
    path('diseases/<pk>/',views.DetailView.as_view(),name='diseasedetail'),
 	path('inputtext/',views.get_text,name='inputtext'),
    path('infoext/',views.info_ext,name='infoext'),
    path('',views.home,name='home'),
       
]