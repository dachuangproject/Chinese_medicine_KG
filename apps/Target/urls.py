from django.urls import path

from apps.Target import views

urlpatterns = [
 path('Targetindex/', views.Targetindex, name='Targetindex'),
 path('Search_target/<str:name>/', views.Search_target, name='Search_target'),
               ]