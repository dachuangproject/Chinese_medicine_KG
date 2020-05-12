from django.shortcuts import render
from django.core.paginator import Paginator
import json
from Graphapp.models import MedMat,Recipe,Molecule,Marker,Illness,Reccom,Herbsmol,Tamol

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
    #TODO:搜索拉丁文名 搜索功能的部分匹配
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
    search_text=request.GET.get('search-com-text')
    if not search_text:
        return render(request,'Comindex.html')
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
    return render(request, 'Comindex.html', {'search_text':search_text,'molecule_list': molecule_list})
def Geneindex(request):
    search_text=request.GET.get('search-gene-text')
    if not search_text:
        return render(request,'Geneindex.html')
    #模糊搜索 检索英文 TODO:检索中文，查询内容有/时报错
    targets=Marker.objects.filter(marker_name__contains=search_text).values_list('marker_name',flat=True)
    #搜索不到
    if not targets:
        return render(request, 'Geneindex.html', {'search_text':search_text})
    p = Paginator(targets,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    target_list = p.get_page(page)
    return render(request, 'Geneindex.html', {'search_text':search_text,'target_list': target_list})
def FAnalyindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'FAnalyindex.html')
    #模糊搜索
    formulas1=Recipe.objects.filter(recipe_name__contains=search_text1).values_list('recipe_name',flat=True)
    formulas2=Recipe.objects.filter(recipe_name__contains=search_text2).values_list('recipe_name',flat=True)
    #没有找到
    if not (formulas1 or formulas2):
        return render(request, 'FAnalyindex.html', {'search_text1':search_text1,'search_text2':search_text2})
    else:
        if not formulas1:
            return render(request, 'FAnalyindex.html', {'search_text1':search_text1})
        else:
            if not formulas2:
                return render(request, 'FAnalyindex.html', {'search_text2':search_text2})
    #组合查询结果
    formulas=[]
    dict={}
    for formula1 in formulas1:
        for formula2 in formulas2:
            if formula1 != formula2:
                if formula1>formula2:
                    formula_item=formula1 +'   '+ formula2
                else:
                    formula_item=formula2 +'   '+ formula1
                dict[formula_item]=True
    for key in dict:
        formulas.append(key)
    p = Paginator(formulas,10)
    page = request.GET.get('page',1)
    formula_list = p.get_page(page)
    return render(request, 'FAnalyindex.html', {'search_text1':search_text1,'search_text2':search_text2, 'formula_list':formula_list})
def FComindex(request):
    search_text=request.GET.get('search-recipe-text')
    if not search_text:
        return render(request,'FComindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'FComindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'FComindex.html', {'search_text':search_text,'recipe_list': recipe_list})
def Predictindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'Predictindex.html')
    #模糊搜索
    herbs1=MedMat.objects.filter(med_mat_name__contains=search_text1).values_list('med_mat_name',flat=True)
    herbs2=MedMat.objects.filter(med_mat_name__contains=search_text2).values_list('med_mat_name',flat=True)
    #没有找到
    if not (herbs1 or herbs2):
        return render(request, 'Predictindex.html', {'search_text1':search_text1,'search_text2':search_text2})
    else:
        if not herbs1:
            return render(request, 'Predictindex.html', {'search_text1':search_text1})
        else:
            if not herbs2:
                return render(request, 'Predictindex.html', {'search_text2':search_text2})
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
    return render(request, 'Predictindex.html', {'search_text1':search_text1,'search_text2':search_text2, 'herb_list':herb_list})
def ADRindex(request):
    return render(request, 'ADRindex.html')
def Analysis(request,name):
    #拆分name
    herb=name.split('   ')
    mols1=Herbsmol.objects.filter(herbs_name=herb[0]).values_list('molecular_name',flat=True)
    mols2=Herbsmol.objects.filter(herbs_name=herb[1]).values_list('molecular_name',flat=True)
    #求交
    mol=set(mols1)&set(mols2)
    tar1=[]
    tar2=[]
    for mol1 in mols1:
        for i in Tamol.objects.filter(molecular_name=mol1).values_list('tg_name',flat=True):
            tar1.append(i)
    for mol2 in mols2:
        for i in Tamol.objects.filter(molecular_name=mol2).values_list('tg_name',flat=True):
            tar2.append(i)
    tar = set(tar1)&set(tar2)
    return render(request, 'Analysis.html', {'mol':mol,'tar':tar,'name':name,'herb1':herb[0],'herb2':herb[1]})
def FAnalysis(request,name):
    #拆分name
    formula=name.split('   ')
    formula1=Recipe.objects.filter(recipe_name=formula[0]).values_list('recipe_no',flat=True)
    formula2=Recipe.objects.filter(recipe_name=formula[1]).values_list('recipe_no',flat=True)
    herbs1=Reccom.objects.filter(recipe_no=formula1[0]).values_list('med_mat_name',flat=True)
    herbs2=Reccom.objects.filter(recipe_no=formula2[0]).values_list('med_mat_name',flat=True)
    mols1=[]
    mols2=[]
    for herb1 in herbs1:
        for i in Herbsmol.objects.filter(herbs_name=herb1).values_list('molecular_name',flat=True):
            mols1.append(i)
    for herb2 in herbs2:
        for i in Herbsmol.objects.filter(herbs_name=herb2).values_list('molecular_name',flat=True):
            mols2.append(i)
    #求交
    mol=set(mols1)&set(mols2)
    tar1=[]
    tar2=[]
    for mol1 in mols1:
        for i in Tamol.objects.filter(molecular_name=mol1).values_list('tg_name',flat=True):
            tar1.append(i)
    for mol2 in mols2:
        for i in Tamol.objects.filter(molecular_name=mol2).values_list('tg_name',flat=True):
            tar2.append(i)
    tar = set(tar1)&set(tar2)
    return render(request, 'FAnalysis.html', {'mol':mol,'tar':tar,'name':name,'formula1':formula[0],'formula2':formula[1],'herbs1':herbs1,'herbs2':herbs2})
def RecipehcKG(request,name):
        recipe=Recipe.objects.filter(recipe_name=name)
        nodes = []
        links = []
        #TODO:查询优化
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].recipe_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=Reccom.objects.filter(recipe_no=recipe[0].recipe_no).values_list('med_mat_name',flat=True)
        #2 查询每种药材对应组分分子 source：药材 target：分子
        for herb in herbs:
            nodes.append({'id': herb, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].recipe_name, 'target': herb, 'value': 3})
            molecules=Herbsmol.objects.filter(herbs_name=herb).values_list('molecular_name',flat=True)
            for molecule in molecules:
                 nodes.append({'id': molecule, 'class': 'Molecule', 'group': 2, 'size': 10})
                 links.append({'source': herb, 'target': molecule, 'value': 3})
        #去重
        node=[]
        for i in nodes:
            if i not in node:
                node.append(i)
        #组合成json字符串
        arg=json.dumps({'nodes': node, 'links': links})
        return render(request,'RecipehcKG.html',{'arg':arg,'recipe_mame':name})
def RecipehmiKG(request,name):
        recipe=Recipe.objects.filter(recipe_name=name)
        nodes = []
        links = []
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].recipe_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=Reccom.objects.filter(recipe_no=recipe[0].recipe_no).values_list('med_mat_name',flat=True)
        #2 查询每个药材对应靶标source：药材 target：靶标
        for herb in herbs:
            nodes.append({'id': herb, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].recipe_name, 'target': herb, 'value': 3})
            molecules=Herbsmol.objects.filter(herbs_name=herb).values_list('molecular_name',flat=True)
            for molecule in molecules:
                targets=Tamol.objects.filter(molecular_name=molecule).values_list('tg_name',flat=True)
                for target in targets:
                    nodes.append({'id': target, 'class': 'Target', 'group': 2, 'size': 10})
                    links.append({'source': herb, 'target': target, 'value': 3})
                 #3 查询每个靶标对应疾病 source：靶标 target：疾病
                    disease=Marker.objects.filter(marker_name=target).values_list('diseasesName',flat=True)
                    if disease:
                        diseaseNames=disease[0].split(';')
                        for diseaseName in diseaseNames:
                            nodes.append({'id': diseaseName, 'class': 'Molecule', 'group': 3, 'size': 8})
                            links.append({'source': target, 'target': diseaseName, 'value': 3})
        #去重
        node=[]
        for i in nodes:
            if i not in node:
                node.append(i)
        #组合成json字符串
        arg=json.dumps({'nodes': node, 'links': links})
        return render(request,'RecipehmiKG.html',{'arg':arg,'recipe_mame':name})
def PredictKG(request,name):
    herbs=name.split('   ')
    nodes = []
    links = []
    #1 查询两个药材对应组分 source：药材 target：组分
    for herb in herbs:
        nodes.append({'id': herb, 'class': 'herb', 'group': 0, 'size': 15})
        molecules=Herbsmol.objects.filter(herbs_name=herb).values_list('molecular_name',flat=True)
        for molecule in molecules:
            nodes.append({'id': molecule, 'class': 'Molecule', 'group': 1, 'size': 12})
            links.append({'source': herb, 'target': molecule, 'value': 3})
            targets=Tamol.objects.filter(molecular_name=molecule).values_list('tg_name',flat=True)
            #2 查询组分对应靶标 source：药材 target：靶标
            for target in targets:
                nodes.append({'id': target, 'class': 'Target', 'group': 2, 'size': 10})
                links.append({'source': herb, 'target': target, 'value': 3})
                #3 查询每个靶标对应疾病 source：靶标 target：疾病
                disease=Marker.objects.filter(marker_name=target).values_list('diseasesName',flat=True)
                if disease:
                    diseaseNames=disease[0].split(';')
                    for diseaseName in diseaseNames:
                        nodes.append({'id': diseaseName, 'class': 'Molecule', 'group': 3, 'size': 8})
                        links.append({'source': target, 'target': diseaseName, 'value': 3})
    #去重
    node=[]
    for i in nodes:
        if i not in node:
            node.append(i)
    #组合成json字符串
    arg=json.dumps({'nodes': node, 'links': links})
    return render(request,'PredictKG.html',{'arg':arg,'herb1':herbs[0],'herb2':herbs[1]})
def Search_recipe(request,name):
    recipe=Recipe.objects.filter(recipe_name=name)
    reccoms=Reccom.objects.filter(recipe_no=recipe[0].recipe_no)
    return render(request, 'Search_recipe.html', {'reccoms':reccoms,'recipe':recipe[0]})
def Search_herb(request,name):
    herb=MedMat.objects.filter(med_mat_name=name)
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
    return render(request, 'Search_herb.html', {'herb':herb[0],'classify':herb[0].medclassify,'molecule_list':molecules,'target_list':targets,'name':name})
def Search_com(request,name):
    molecule=Molecule.objects.filter(molecule_name=name)
    # field_list = []
    # dict={}
    # for field in Molecule._meta.fields():
    #       dict[field.name] = field.verbose_name
    # print(dict)
    # #print(getattr(molecule[0],'ML'))
    if not molecule:
        return render(request, 'Search_com.html', {'name':name})
    return render(request, 'Search_com.html', {'molecule':molecule[0],'name':name})
def Search_target(request,name):
    target=Marker.objects.filter(marker_name=name)
    if not target:
        return render(request, 'Search_target.html', {'name':name})
    diseases=target[0].diseasesName.split(';')
    return render(request, 'Search_target.html', {'target':target[0],'diseases':diseases,'name':name})
def FCom(request,name):
    recipe=Recipe.objects.filter(recipe_name=name)
    reccoms=Reccom.objects.filter(recipe_no=recipe[0].recipe_no).values_list('med_mat_name',flat=True)
    return render(request, 'FCom.html', {'reccoms':reccoms,'recipe':recipe[0]})