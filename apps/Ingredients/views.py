from django.core.paginator import Paginator
from django.shortcuts import render

from apps.Graphapp.models import Molecule

# Create your views here.


def Comindex(request):
    search_text=request.GET.get('search-com-text')
    if not search_text:
        return render(request, 'Comindex.html')
    #模糊搜索 检索英文 TODO:检索中文
    molecule=Molecule.objects.filter(molecule_name__contains=search_text)
    #搜索不到
    if not molecule:
        return render(request, 'Comindex.html', {'search_text':search_text})
    p = Paginator(molecule,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    molecule_list = p.get_page(page)
    return render(request, 'Comindex.html', {'search_text':search_text, 'molecule_list': molecule_list})
def Search_com(request,name):
    molecule=Molecule.objects.filter(molecule_name=name)
    if not molecule:
        return render(request, 'Search_com.html', {'name':name})
    return render(request, 'Search_com.html', {'molecule':molecule[0], 'name':name})