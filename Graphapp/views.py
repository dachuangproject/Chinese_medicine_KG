from django.shortcuts import render
from django.core.paginator import Paginator
import json
from Graphapp.models import MedMat,Recipe,Molecule,Marker,Illness

def index(request):
    search_text=request.GET.get('search-recipe-text')
    if not search_text:
        return render(request,'index.html')
    #TODO: 搜索拉丁文名
    #模糊搜索 
    recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'index.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'index.html', {'search_text':search_text,'recipe_list': recipe_list})
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
def herbindex(request):
    search_text=request.GET.get('search-herb-text')
    if not search_text:
        return render(request,'herbindex.html')
    #TODO:搜索拉丁文名
    herbs=MedMat.objects.filter(med_mat_name__contains=search_text)
    #搜索不到
    if not herbs:
        return render(request, 'herbindex.html', {'search_text':search_text})
    p = Paginator(herbs,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    herb_list = p.get_page(page)
    return render(request, 'herbindex.html', {'search_text':search_text, 'herb_list':herb_list})
def Analysisindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'Analysisindex.html')
    #模糊搜索
    herbs1=MedMat.objects.filter(med_mat_name__contains=search_text1).values_list('med_mat_name',flat=True)
    herbs2=MedMat.objects.filter(med_mat_name__contains=search_text2).values_list('med_mat_name',flat=True)
    #没有找到
    if not (herbs1 or herbs2):
        return render(request, 'Analysisindex.html', {'search_text1':search_text1,'search_text2':search_text2})
    else:
        if not herbs1:
            return render(request, 'Analysisindex.html', {'search_text1':search_text1})
        else:
            if not herbs2:
                return render(request, 'Analysisindex.html', {'search_text2':search_text2})
    #组合查询结果
    herbs=[]
    dict={}
    for herb1 in herbs1:
        for herb2 in herbs2:
            if herb1 != herb2:
                if herb1>herb2:
                    herb_item=herb1 +'   '+ herb2
                else:
                    herb_item=herb2 +'   '+ herb1
                dict[herb_item]=True
    for key in dict:
        herbs.append(key)
    p = Paginator(herbs,10)
    page = request.GET.get('page',1)
    herb_list = p.get_page(page)
    return render(request, 'Analysisindex.html', {'search_text1':search_text1,'search_text2':search_text2, 'herb_list':herb_list})
def Recipehcindex(request):
    search_text=request.GET.get('search-recipehcKG-text')
    if not search_text:
        return render(request,'Recipehcindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'Recipehcindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'Recipehcindex.html', {'search_text':search_text,'recipe_list':recipe_list})
def Recipehmiindex(request):
    search_text=request.GET.get('search-recipehmiKG-text')
    if not search_text:
        return render(request,'Recipehmiindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'Recipehmiindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'Recipehmiindex.html', {'search_text':search_text,'recipe_list':recipe_list})
def Comindex(request):
    # search_text=request.GET.get('search-com-text')
    # if not search_text:
    #     return render(request,'Comindex.html')
    # #模糊搜索
    # recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    # #搜索不到
    # if not recipes:
    #     return render(request, 'index.html', {'search_text':search_text})
    return render(request, 'Comindex.html')
def Geneindex(request):
    # search_text=request.GET.get('search-gene-text')
    # if not search_text:
    #     return render(request,'index.html')
    # #TODO: 搜索拉丁文名
    # #模糊搜索
    # recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    # #搜索不到
    # if not recipes:
    #     return render(request, 'index.html', {'search_text':search_text})
    return render(request, 'Geneindex.html')
def ADRindex(request):
    return render(request, 'ADRindex.html')
def Analysis(request,name):
    #拆分name
    herb=name.split('   ')
    herb1=MedMat.objects.filter(med_mat_name=herb[0])
    herb2=MedMat.objects.filter(med_mat_name=herb[1])
    #TODO：求交集
    qs_com = Molecule.objects.filter(med_mat_no__in=['herb1.med_mat_no','herb2.med_mat_no'])
    qs_marker = Marker.objects.filter(med_mat_no__in=['herb1.med_mat_no','herb2.med_mat_no'])
    return render(request, 'Analysis.html', {'coms':qs_com,'markers':qs_marker,'name':name})
def Search_recipe(request,name):
    recipe=Recipe.objects.filter(recipe_name=name)
    herbs=MedMat.objects.filter(recipe_no=recipe[0].recipe_no)
    return render(request, 'Search_recipe.html', {'herbs':herbs,'recipe':recipe[0]})
def RecipehcKG(request,name):
        recipe=Recipe.objects.filter(recipe_name=name)
        nodes = []
        links = []
        #TODO:查询优化
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].recipe_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=MedMat.objects.filter(recipe_no=recipe[0].recipe_no)
        #2 查询每种药材对应组分分子 查询每个药材对应靶标source：药材 target：分子/靶标
        for herb in herbs:
            nodes.append({'id': herb.med_mat_name, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].recipe_name, 'target': herb.med_mat_name, 'value': 3})
            Com_Molecules=Molecule.objects.filter(med_mat_no=herb.med_mat_no)
            for Com_Molecule in Com_Molecules:
                nodes.append({'id': Com_Molecule.molecule_name, 'class': 'Molecule', 'group': 2, 'size': 15})
                links.append({'source': herb.med_mat_name, 'target': Com_Molecule.molecule_name, 'value': 3})
        #组合成json字符串
        arg=json.dumps({'nodes': nodes, 'links': links})
        return render(request,'RecipehcKG.html',{'arg':arg})
def RecipehmiKG(request,name):
        recipe=Recipe.objects.filter(recipe_name=name)
        nodes = []
        links = []
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].recipe_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=MedMat.objects.filter(recipe_no=recipe[0].recipe_no)
        #2 查询每个药材对应靶标source：药材 target：靶标
        for herb in herbs:
            nodes.append({'id': herb.med_mat_name, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].recipe_name, 'target': herb.med_mat_name, 'value': 3})
            markers=Marker.objects.filter(med_mat_no=herb.med_mat_no)
            for marker in markers:
                 nodes.append({'id': marker.marker_name, 'class': 'Marker', 'group': 2, 'size': 8})
                 links.append({'source': herb.med_mat_name, 'target': marker.marker_name, 'value': 3})
                #3 查询每个靶标对应疾病 source：靶标 target：疾病
                 illness=Illness.objects.filter(illness_no=marker.illness_no)
                 for illness_item in illness:
                     nodes.append({'id': illness_item.illness_name, 'class': 'Molecule', 'group': 3, 'size': 8})
                     links.append({'source': marker.marker_name, 'target': illness_item.illness_name, 'value': 3})
        #组合成json字符串
        arg=json.dumps({'nodes': nodes, 'links': links})
        return render(request,'RecipehmiKG.html',{'arg':arg})
def Search_herb(request,name):
    herb=MedMat.objects.filter(med_mat_name=name)
    return render(request, 'Search_herb.html', {'herb':herb[0],'classify':herb[0].medclassify})