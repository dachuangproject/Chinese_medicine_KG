from django.contrib import admin
from django.urls import path
from Graphapp import views

urlpatterns = [
 #方剂信息展示页面
 path('Search_recipe/(?P<name>\w+)', views.Search_recipe, name='Search_recipe'),
 path('index/', views.index, name='index'),
 #不良反应
 path('ADRindex/', views.ADRindex, name='ADRindex'),
 #方剂KG搜索页面
 path('Recipehcindex/', views.Recipehcindex, name='Recipehcindex'),
 path('Recipehmiindex/', views.Recipehmiindex, name='Recipehmiindex'),
 #方剂KG展示
 path('RecipehcKG/(?P<name>\w+)', views.RecipehcKG, name='RecipehcKG'),
 path('RecipehmiKG/(?P<name>\w+)', views.RecipehmiKG, name='RecipehmiKG'),
 #查询分析
 path('Analysisindex/', views.Analysisindex, name='Analysisindex'),
 path('Analysis/(?P<name>\w+)', views.Analysis, name='Analysis'),
 #药材信息展示页面
 path('herbindex/', views.herbindex, name='herbindex'),
 path('Search_herb/(?P<name>\w+)', views.Search_herb, name='Search_herb'),
 #组分
 path('Comindex/', views.Comindex, name='Comindex'),
 #基因
 path('Geneindex/', views.Geneindex, name='Geneindex'),
]