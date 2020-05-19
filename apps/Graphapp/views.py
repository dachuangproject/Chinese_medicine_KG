import json

from django.core.paginator import Paginator
from django.shortcuts import render

from apps.Graphapp.models import Herbs,Formulas,Target,Forcom,Herbsmol,Tamol
#药材组分知识图谱
def Recipehcindex(request):
    search_text=request.GET.get('search-recipehcKG-text')
    if not search_text:
        return render(request,'Recipehcindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text).values_list('formulas_name',flat=True)
    #搜索不到
    if not recipes:
        return render(request, 'Recipehcindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'Recipehcindex.html', {'search_text':search_text,'recipe_list':recipe_list})
def RecipehcKG(request,name):
        recipe=Formulas.objects.filter(formulas_name=name)
        nodes = []
        links = []
        #TODO:查询优化
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].formulas_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=Forcom.objects.filter(formulas_no=recipe[0].formulas_no).values_list('herbs_name',flat=True)
        #2 查询每种药材对应组分分子 source：药材 target：分子
        for herb in herbs:
            nodes.append({'id': herb, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].formulas_name, 'target': herb, 'value': 3})
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
#药材靶标疾病知识图谱
def RecipehmiKG(request,name):
        recipe=Formulas.objects.filter(formulas_name=name)
        nodes = []
        links = []
        #1 查询该方剂对应所有药材 source：方剂 target：药材 node：药材
        nodes.append({'id': recipe[0].formulas_name, 'class': 'recipe', 'group': 0, 'size': 20})
        herbs=Forcom.objects.filter(formulas_no=recipe[0].formulas_no).values_list('formulas_name',flat=True)
        #2 查询每个药材对应靶标source：药材 target：靶标
        for herb in herbs:
            nodes.append({'id': herb, 'class': 'herb', 'group': 1, 'size': 15})
            links.append({'source': recipe[0].formulas_name, 'target': herb, 'value': 3})
            molecules=Herbsmol.objects.filter(herbs_name=herb).values_list('molecular_name',flat=True)
            for molecule in molecules:
                targets=Tamol.objects.filter(molecular_name=molecule).values_list('tg_name',flat=True)
                for target in targets:
                    nodes.append({'id': target, 'class': 'Target', 'group': 2, 'size': 10,'activesize':15})
                    links.append({'source': herb, 'target': target, 'value': 3})
                 #3 查询每个靶标对应疾病 source：靶标 target：疾病
                    disease=Target.objects.filter(target_name=target).values_list('diseasesName',flat=True)
                    if disease:
                        diseaseNames=disease[0].split(';')
                        for diseaseName in diseaseNames:
                            nodes.append({'id': diseaseName, 'class': 'Molecule', 'group': 3, 'size': 8,'activesize':13})
                            links.append({'source': target, 'target': diseaseName, 'value': 3})
        #去重
        node=[]
        for i in nodes:
            if i not in node:
                node.append(i)
        #组合成json字符串
        arg=json.dumps({'nodes': node, 'links': links})
        return render(request,'RecipehmiKG.html',{'arg':arg,'recipe_mame':name})
def Recipehmiindex(request):
    search_text=request.GET.get('search-recipehmiKG-text')
    if not search_text:
        return render(request,'Recipehmiindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Formulas.objects.filter(formulas_name__contains=search_text).values_list('formulas_name',flat=True)
    #搜索不到
    if not recipes:
        return render(request, 'Recipehmiindex.html', {'search_text':search_text})
    p = Paginator(recipes,10)   #分页，10个一页
    # 获取 url 中的页码
    page = request.GET.get('page',1)
    # 将导航对象相应的页码内容返回给 articles
    recipe_list = p.get_page(page)
    return render(request, 'Recipehmiindex.html', {'search_text':search_text,'recipe_list':recipe_list})
#药对配伍界面
def Predictindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'Predictindex.html')
    #模糊搜索
    herbs1=Herbs.objects.filter(herbs_name__contains=search_text1).values_list('herbs_name',flat=True)
    herbs2=Herbs.objects.filter(herbs_name__contains=search_text2).values_list('herbs_name',flat=True)
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
                disease=Target.objects.filter(target_name=target).values_list('diseasesName',flat=True)
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

