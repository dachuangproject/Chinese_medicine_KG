from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from Graphapp.models import MedMat,Recipe

def index(request):
    return render(request,'index.html')
def herb(request):
    return render(request, 'Recipe.html')
def target(request):
    return render(request,'target.html')
def Search_recipe(request):
    search_text=request.GET['search-recipe-text']
    if not search_text:
        return render(request,'index.html')
    #TODO:扩展搜索范围 搜索拉丁文名
    recipe=Recipe.objects.filter(recipe_name=search_text)
    #搜索不到
    if not recipe:
        return render(request, 'Search_recipe.html', {'search_text':search_text})
    herbs=MedMat.objects.filter(recipe_no=recipe[0].recipe_no)
    # herbs_count=MedMat.objects.count(recipe_no=recipe[0].recipe_no)
    return render(request, 'Search_recipe.html', {'recipe':recipe[0], 'herbs':herbs})