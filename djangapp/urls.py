
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('index/',views.index),
    path('index1/', views.index1),
    path('show/', views.show),
    
    path('index2/',views.index2),
    path('index3/', views.index3),
    path('index4/', views.index4),
    path('index5/', views.index5),
    path('index6/',views.index6),
    path('info/', views.methodinfo),
    path('info1/', views.methodinfo1),
    path('info2/', views.methodinfo2),
    path('get',views.getdata),
    path('ssession',views.setsession),  
    path('gsession',views.getsession),
     path('scookie',views.setcookie),  
    path('gcookie',views.getcookie) ,
    path('csv',views.getfile),
    path('csv1',views.getfile1) ,

]
