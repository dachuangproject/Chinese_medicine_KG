from django.urls import path

from apps.Herb import views

urlpatterns = [
        #药材信息展示页面
 path('herbindex/', views.herbindex, name='herbindex'),
 path('Search_herb/(?P<name>\w+)', views.Search_herb, name='Search_herb')
 ]