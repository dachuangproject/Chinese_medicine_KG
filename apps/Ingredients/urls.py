from django.urls import path

from apps.Ingredients import views

urlpatterns = [
         #组分
 path('Comindex/', views.Comindex, name='Comindex'),
 path('Search_com/(?P<name>\w+)', views.Search_com, name='Search_com'),
         ]