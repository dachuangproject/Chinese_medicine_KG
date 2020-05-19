from django.urls import path

from apps.Graphapp import views

urlpatterns = [
 #方剂KG搜索页面
 path('Recipehcindex/', views.Recipehcindex, name='Recipehcindex'),
 path('Recipehmiindex/', views.Recipehmiindex, name='Recipehmiindex'),
 #方剂KG展示
 path('RecipehcKG/(?P<name>\w+)', views.RecipehcKG, name='RecipehcKG'),
 path('RecipehmiKG/(?P<name>\w+)', views.RecipehmiKG, name='RecipehmiKG'),


 path('Predictindex/', views.Predictindex, name='Predictindex'),
 path('PredictKG/(?P<name>\w+)', views.PredictKG, name='PredictKG'),
]