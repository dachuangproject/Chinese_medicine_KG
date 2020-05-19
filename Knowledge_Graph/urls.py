"""Knowledge_Graph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #图谱展示
    path('Graphapp/', include(('apps.Graphapp.urls',"Graphapp"),namespace='Graphapp')),
    #成分对比分析
    path('Analysis/', include(('apps.Analysis.urls',"Analysis"),namespace='Analysis')),
    #方剂知识库
    path('Formula/', include(('apps.Formula.urls',"Formula"),namespace='Formula')),
    #药材知识库
    path('Herb/', include(('apps.Herb.urls',"Herb"),namespace='Herb')),
    #组分知识库
    path('Ingredients/', include(('apps.Ingredients.urls',"Ingredients"),namespace='Ingredients')),
    #靶标知识库
    path('Target/', include(('apps.Target.urls',"Target"),namespace='Target')),
    #方剂配伍
    path('Combination/', include(('apps.Combination.urls',"Combination"),namespace='Combination'))
  ]