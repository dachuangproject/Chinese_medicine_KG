from django.urls import path

from apps.Combination import views

urlpatterns = [
 path('FComindex/', views.FComindex, name='FComindex'),
 path('FCom/(?P<name>\w+)', views.FCom, name='FCom')
 ]