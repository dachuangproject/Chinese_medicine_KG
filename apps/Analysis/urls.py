from django.urls import path

from apps.Analysis import views

urlpatterns = [
#查询分析
 path('Analysisindex/', views.Analysisindex, name='Analysisindex'),
 path('Analysis/<str:name>/', views.Analysis, name='Analysis'),

 path('FAnalyindex/', views.FAnalyindex, name='FAnalyindex'),
 path('FAnalysis/<str:name>/', views.FAnalysis, name='FAnalysis')
]