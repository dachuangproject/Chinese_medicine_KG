from django.core.paginator import Paginator
from django.shortcuts import render
import json
from apps.Graphapp.models import Herbs,Formulas,Forcom,Herbsmol,Tamol

#药材对比分析
def Analysisindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'Analysisindex.html')
    #模糊搜索
    herbs1=Herbs.objects.filter(herbs_name__contains=search_text1).values_list('herbs_name',flat=True)
    herbs2=Herbs.objects.filter(herbs_name__contains=search_text2).values_list('herbs_name',flat=True)
    #没有找到
    if not (herbs1 or herbs2):
        return render(request, 'Analysisindex.html', {'search_text1':search_text1, 'search_text2':search_text2})
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
    return render(request, 'Analysisindex.html', {'search_text1':search_text1, 'search_text2':search_text2, 'herb_list':herb_list})
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
    return render(request, 'Analysis.html', {'mol':mol, 'tar':tar, 'name':name, 'herb1':herb[0], 'herb2':herb[1]})
#方剂对比分析
def FAnalyindex(request):
    search_text1=request.GET.get('search-text1')
    search_text2=request.GET.get('search-text2')
    if not (search_text1 or search_text2):
        return render(request, 'FAnalyindex.html')
    #模糊搜索
    formulas1=Formulas.objects.filter(formulas_name__contains=search_text1).values_list('formulas_name',flat=True)
    formulas2=Formulas.objects.filter(formulas_name__contains=search_text2).values_list('formulas_name',flat=True)
    #没有找到
    if not (formulas1 or formulas2):
        return render(request, 'FAnalyindex.html', {'search_text1':search_text1, 'search_text2':search_text2})
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
    return render(request, 'FAnalyindex.html', {'search_text1':search_text1, 'search_text2':search_text2, 'formula_list':formula_list})
def FAnalysis(request,name):
    #拆分name
    formula=name.split('   ')
    nodes = []
    links = []
    nodes.append({'id': formula[0], 'class': 'recipe', 'group': 0, 'size': 20})
    nodes.append({'id': formula[1], 'class': 'recipe', 'group': 0, 'size': 20})
    formula1=Formulas.objects.filter(formulas_name=formula[0]).values_list('formulas_no',flat=True)
    formula2=Formulas.objects.filter(formulas_name=formula[1]).values_list('formulas_no',flat=True)
    herbs1=Forcom.objects.filter(formulas_no=formula1[0]).values_list('herbs_name',flat=True)
    herbs2=Forcom.objects.filter(formulas_no=formula2[0]).values_list('herbs_name',flat=True)
    mols1=[]
    mols2=[]
    for herb1 in herbs1:
        nodes.append({'id': herb1, 'class': 'herb', 'group': 1, 'size': 15})
        links.append({'source': formula[0], 'target': herb1, 'value': 3})
        for i in Herbsmol.objects.filter(herbs_name=herb1).values_list('molecular_name',flat=True):
            mols1.append(i)
    for herb2 in herbs2:
        nodes.append({'id': herb2, 'class': 'herb', 'group': 1, 'size': 15})
        links.append({'source': formula[1], 'target': herb2, 'value': 3})
        for i in Herbsmol.objects.filter(herbs_name=herb2).values_list('molecular_name',flat=True):
            mols2.append(i)
    #去重
    node=[]
    for i in nodes:
        if i not in node:
            node.append(i)
    nodes=node
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
    #添加共同靶标
    for tar_item in tar:
        nodes.append({'id': tar_item, 'class': 'Target', 'group': 3, 'size': 10})
        for i in Tamol.objects.filter(tg_name=tar_item).values_list('molecular_name',flat=True):
            for j in Herbsmol.objects.filter(molecular_name=i).values_list('herbs_name',flat=True):
                if (j in (herbs1 or herbs2)):
                    links.append({'source': j, 'target': tar_item, 'value': 3})
     #添加共同组分
    for mol_item in mol:
        nodes.append({'id': mol_item, 'class': 'Molecule', 'group': 2, 'size': 10})
        for i in Herbsmol.objects.filter(molecular_name=mol_item).values_list('herbs_name',flat=True):
             if (i in (herbs1 or herbs2)):
                links.append({'source': i, 'target': mol_item, 'value': 3})
    #组合成json字符串
    arg=json.dumps({'nodes': nodes, 'links': links})
    return render(request, 'FAnalysis.html', {'mol':mol, 'tar':tar, 'name':name, 'formula1':formula[0], 'formula2':formula[1], 'herbs1':herbs1, 'herbs2':herbs2,'arg':arg})
