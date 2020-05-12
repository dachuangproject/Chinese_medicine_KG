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

 path('FAnalyindex/', views.FAnalyindex, name='FAnalyindex'),
 path('FAnalysis/(?P<name>\w+)', views.FAnalysis, name='FAnalysis'),
 #药材信息展示页面
 path('herbindex/', views.herbindex, name='herbindex'),
 path('Search_herb/(?P<name>\w+)', views.Search_herb, name='Search_herb'),
 #组分
 path('Comindex/', views.Comindex, name='Comindex'),
 path('Search_com/(?P<name>\w+)', views.Search_com, name='Search_com'),
 #基因
 path('Geneindex/', views.Geneindex, name='Geneindex'),
 path('Search_target/(?P<name>\w+)', views.Search_target, name='Search_target'),

 path('FComindex/', views.FComindex, name='FComindex'),
 path('FCom/(?P<name>\w+)', views.FCom, name='FCom'),

 path('Predictindex/', views.Predictindex, name='Predictindex'),
 path('PredictKG/(?P<name>\w+)', views.PredictKG, name='PredictKG'),
]