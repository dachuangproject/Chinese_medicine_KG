from django.urls import path

from apps.Target import views

urlpatterns = [
 path('Targetindex/', views.Targetindex, name='Targetindex'),
 path('Search_target/(?P<name>\w+)', views.Search_target, name='Search_target'),
               ]