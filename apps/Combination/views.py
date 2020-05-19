from django.core.paginator import Paginator
from django.shortcuts import render

from apps.Graphapp.models import Formulas,Forcom

# Create your views here.

#加减化裁界面
def FCom(request,name):
    recipe=Formulas.objects.filter(formulas_name=name)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no).values_list('herbs_name',flat=True)
    return render(request, 'FCom.html', {'reccoms':reccoms, 'recipe':recipe[0]})
def FComindex(request):
    search_text=request.GET.get('search-recipe-text')
    if not search_text:
        return render(request, 'FComindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'FComindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'FComindex.html', {'search_text':search_text, 'recipe_list': recipe_list})
