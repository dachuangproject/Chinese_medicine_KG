
from django.contrib import admin
from django.urls import path
from Graphapp import views

urlpatterns = [
 path('Search_recipe/', views.Search_recipe, name='Search_recipe'),
 path('index/', views.index, name='index'),
 path('target/', views.target, name='target'),
 path('herb/', views.herb, name='herb'),
]