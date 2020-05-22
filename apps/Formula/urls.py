from django.urls import path
from apps.Formula import views


urlpatterns = [
 #方剂信息展示页面
 path('Search_recipe/<str:name>', views.Search_recipe, name='Search_recipe'),
 path('index/', views.index, name='index'),
  #不良反应
 path('ADRindex/', views.ADRindex, name='ADRindex'),
 path('ADR/<str:name>', views.ADR, name='ADR')
 ]