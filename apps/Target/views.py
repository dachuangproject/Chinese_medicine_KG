from django.core.paginator import Paginator
from django.shortcuts import render

from apps.Graphapp.models import Target
# Create your views here.

def Targetindex(request):
    search_text=request.GET.get('search-gene-text')
    if not search_text:
        return render(request, 'Targetindex.html')
    #模糊搜索 检索英文 TODO:检索中文，查询内容有/时报错
    targets=Target.objects.filter(target_name__contains=search_text).values_list('target_name',flat=True)
    #搜索不到
    if not targets:
        return render(request, 'Targetindex.html', {'search_text':search_text})
    p = Paginator(targets,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    target_list = p.get_page(page)
    return render(request, 'Targetindex.html', {'search_text':search_text, 'target_list': target_list})
def Search_target(request,name):
    target=Target.objects.filter(target_name=name)
    if not target:
        return render(request, 'Search_target.html', {'name':name})
    diseases=target[0].diseasesName.split(';')
    return render(request, 'Search_target.html', {'target':target[0], 'diseases':diseases, 'name':name})