from django.core.paginator import Paginator
from django.shortcuts import render
from apps.Graphapp.models import Formulas, Forcom,Herbs
# Create your views here.

#方剂知识库
def index(request):
    search_text=request.GET.get('search-recipe-text')
    if not search_text:
        return render(request, 'index.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text,mark=1).values_list('formulas_name',flat=True)
    #搜索不到
    if not recipes:
        return render(request, 'index.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'index.html', {'search_text':search_text, 'recipe_list': recipe_list})
def Search_recipe(request,name):
    recipe=Formulas.objects.filter(formulas_name=name,mark=1)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no,mark=1)
    return render(request, 'Search_recipe.html', {'reccoms':reccoms, 'recipe':recipe[0]})
#不良反应界面
def ADRindex(request):
    search_text=request.GET.get('search-text')
    if not search_text:
        return render(request, 'ADRindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text,mark=1).values_list('formulas_name',flat=True)
    #搜索不到
    if not recipes:
        return render(request, 'ADRindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'ADRindex.html', {'search_text':search_text, 'recipe_list': recipe_list})
def ADR(request,name):
    recipe=Formulas.objects.filter(formulas_name=name,mark=1)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no,mark=1).values_list('herbs_name',flat=True)
    herbs={}
    for reccom in reccoms:
        herb=Herbs.objects.filter(herbs_name=reccom)
        if herb:
            if herb[0].adverserea == 'null':
                herb[0].adverserea='暂无'
                herbs[herb[0].herbs_name]=herb[0].adverserea
    return render(request, 'ADR.html', {'recipe':recipe[0],'herbs':herbs})
