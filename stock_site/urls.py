from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome , name='welcome') , 
    path('home/', views.home , name='home') , 
    path('chart/', views.chart , name='chart') ,
    path('news/', views.news , name='news')
]
