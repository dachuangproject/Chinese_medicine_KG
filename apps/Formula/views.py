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
    recipes=Formulas.objects.filter(formulas_name__contains=search_text).values_list('formulas_name',flat=True)
    #搜索不到
    if not recipes:
        return render(request, 'index.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'index.html', {'search_text':search_text, 'recipe_list': recipe_list})
    # if p.num_pages <= 1:  #如果不足一页
    #     recipe_list = recipes  #直接返回所有
    #     data = ''  #不需要分页按钮
    # else:
    #     page = int(request.GET.get('page',1))  #获取请求的文章页码，默认为第一页
    #     print(page)
    #     recipe_list = p.page(page) #返回指定页码的页面
    #     left = []  # 当前页左边连续的页码号，初始值为空
    #     right = []  # 当前页右边连续的页码号，初始值为空
    #     left_has_more = False  # 标示第 1 页页码后是否需要显示省略号
    #     right_has_more = False  # 标示最后一页页码前是否需要显示省略号
    #     first = False   # 标示是否需要显示第 1 页的页码号。
    #     # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
    #     # 其它情况下第一页的页码是始终需要显示的。
    #     # 初始值为 False
    #     last = False  # 标示是否需要显示最后一页的页码号。
    #     total_pages = p.num_pages
    #     page_range = p.page_range
    #     if page == 1:  #如果请求第1页
    #         right = page_range[page:page+2]  #获取右边连续号码页
    #         print(total_pages)
    #         if right[-1] < total_pages - 1:    # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
    #         # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
    #             right_has_more = True
    #         if right[-1] < total_pages:   # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
    #         # 所以需要显示最后一页的页码号，通过 last 来指示
    #             last = True
    #     elif page == total_pages:  #如果请求最后一页
    #         left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  #获取左边连续号码页
    #         if left[0] > 2:
    #             left_has_more = True  #如果最左边的号码比2还要大，说明其与第一页之间还有其他页码，因此需要显示省略号，通过 left_has_more 来指示
    #         if left[0] > 1: #如果最左边的页码比1要大，则要显示第一页，否则第一页已经被包含在其中
    #             first = True
    #     else:  #如果请求的页码既不是第一页也不是最后一页
    #         left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   #获取左边连续号码页
    #         right = page_range[page:page+2] #获取右边连续号码页
    #         if left[0] > 2:
    #             left_has_more = True
    #         if left[0] > 1:
    #             first = True
    #         if right[-1] < total_pages - 1:
    #             right_has_more = True
    #         if right[-1] < total_pages:
    #             last = True
    #     data = {    #将数据包含在data字典中
    #         'left':left,
    #         'right':right,
    #         'left_has_more':left_has_more,
    #         'right_has_more':right_has_more,
    #         'first':first,
    #         'last':last,
    #         'total_pages':total_pages,
    #         'page':page
    #     }
    # return render(request, 'index.html', {'search_text':search_text,'recipe_list':recipe_list,'data':data})
def Search_recipe(request,name):
    recipe=Formulas.objects.filter(formulas_name=name)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no)
    return render(request, 'Search_recipe.html', {'reccoms':reccoms, 'recipe':recipe[0]})
#不良反应界面
def ADRindex(request):
    search_text=request.GET.get('search-text')
    if not search_text:
        return render(request, 'ADRindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text).values_list('formulas_name',flat=True)
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
    recipe=Formulas.objects.filter(formulas_name=name)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no).values_list('herbs_name',flat=True)
    herbs={}
    for reccom in reccoms:
        herb=Herbs.objects.filter(herbs_name=reccom)
        if herb:
            if herb[0].adverserea == 'null':
                herb[0].adverserea='暂无'
                herbs[herb[0].herbs_name]=herb[0].adverserea
    return render(request, 'ADR.html', {'recipe':recipe[0],'herbs':herbs})
