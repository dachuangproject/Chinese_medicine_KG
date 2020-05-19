import json

from django.core.paginator import Paginator
from django.shortcuts import render

from apps.Graphapp.models import Herbs,Herbsmol,Tamol

# Create your views here.

def herbindex(request):
    search_text=request.GET.get('search-herb-text')
    if not search_text:
        return render(request, 'herbindex.html')
    #TODO:搜索拉丁文名 搜索功能的部分匹配
    herbs=Herbs.objects.filter(herbs_name__contains=search_text)
    #搜索不到
    if not herbs:
        return render(request, 'herbindex.html', {'search_text':search_text})
    p = Paginator(herbs,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    herb_list = p.get_page(page)
    return render(request, 'herbindex.html', {'search_text':search_text, 'herb_list':herb_list})
def Search_herb(request,name):
    herb=Herbs.objects.filter(herbs_name=name)
    if not herb:
        return render(request, 'Search_herb.html', {'name':name})
    molecules=Herbsmol.objects.filter(herbs_name=name).values_list('molecular_name',flat=True)
    #TODO:分页
    # p = Paginator(molecules,10)   #分页，10个一页
    # # 获取 url 中的页码
    # page1 = request.GET.get('page1')
    # molecule_list = p.get_page(page1)
    targets=[]
    for molecule in molecules:
        for index in Tamol.objects.filter(molecular_name=molecule).values_list('tg_name',flat=True):
            targets.append(index)
    # p = Paginator(targets,10)
    # page2 = request.GET.get('page2')
    # target_list = p.get_page(page2)
    #判定是否在换页
    #if page1:
    #    return render(request, 'Search_herb.html', {'herb':herb[0],'classify':herb[0].medclassify,'molecule_list':molecule_list,'target_list':target_list,'page1':page1})
    #else:
    return render(request, 'Search_herb.html', {'herb':herb[0], 'classify':herb[0].medclassify, 'molecule_list':molecules, 'target_list':targets, 'name':name})
