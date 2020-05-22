from django.urls import path

from apps.Combination import views

urlpatterns = [
 path('FComindex/', views.FComindex, name='FComindex'),
 path('FCom/<str:name>/', views.FCom, name='FCom'),
 # path('FComnew/', views.FComnew, name='FComnew'),
 # path('FCom/<str:name>/form', views.FComnew, name='FComnew'),
 ]