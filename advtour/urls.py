import imp
from django.urls import path
from . import views
app_name='advtour'
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about, name='about'),
    path('gridview/', views.gridview, name='gridview')
]