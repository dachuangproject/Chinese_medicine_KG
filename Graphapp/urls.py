
from django.contrib import admin
from django.urls import path
from Graphapp import views

urlpatterns = [
 #方剂信息展示页面
 path('Search_recipe/(?P<name>\w+)', views.Search_recipe, name='Search_recipe'),
 path('index/', views.index, name='index'),
 #靶标KG搜索页面
 path('Targetindex/', views.Targetindex, name='Targetindex'),
 # path('TargetKG/', views.RecipeKG, name='TargetKG'),
 #方剂KG搜索页面
 path('Recipeindex/', views.Recipeindex, name='Recipeindex'),
 #方剂KG展示
 path('RecipeKG/(?P<name>\w+)', views.RecipeKG, name='RecipeKG'),
 path('herbindex/', views.herbindex, name='herbindex'),
#药材信息展示页面
 path('Search_herb/(?P<name>\w+)', views.Search_herb, name='Search_herb'),
 path('Comindex/', views.Comindex, name='Comindex'),
 path('Geneindex/', views.Geneindex, name='Geneindex'),
]