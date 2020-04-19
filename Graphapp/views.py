from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, 'index.html', {'search_text':search_text,'recipes':recipes})
def herbindex(request):
    search_text=request.GET.get('search-herb-text')
    if not search_text:
        return render(request,'herbindex.html')
    #TODO:搜索拉丁文名
    herbs=MedMat.objects.filter(med_mat_name__contains=search_text)
    #搜索不到
    if not herbs:
        return render(request, 'herbindex.html', {'search_text':search_text})
    return render(request, 'herbindex.html', {'search_text':search_text, 'herbs':herbs})
def Recipeindex(request):
    search_text=request.GET.get('search-recipeKG-text')
    if not search_text:
        return render(request,'Recipeindex.html')
    #TODO: 搜索拉丁文名
    #模糊搜索
    recipes=Recipe.objects.filter(recipe_name__contains=search_text)
    #搜索不到
    if not recipes:
        return render(request, 'Recipeindex.html', {'search_text':search_text})
    return render(request, 'Recipeindex.html', {'search_text':search_text,'recipes':recipes})
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
def Targetindex(request):
    return render(request, 'Targetindex.html')
def Search_recipe(request,name):
    recipe=Recipe.objects.filter(recipe_name=name)
    herbs=MedMat.objects.filter(recipe_no=recipe[0].recipe_no)
    return render(request, 'Search_recipe.html', {'herbs':herbs,'recipe':recipe[0]})
def RecipeKG(request,name):
        recipe=Recipe.objects.filter(recipe_name=name)
        nodes = []
        links = []
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
            markers=Marker.objects.filter(med_mat_no=herb.med_mat_no)
            for marker in markers:
                 nodes.append({'id': marker.marker_name, 'class': 'Marker', 'group': 3, 'size': 8})
                 links.append({'source': herb.med_mat_name, 'target': marker.marker_name, 'value': 3})
                #3 查询每个靶标对应疾病 source：靶标 target：疾病
                 illness=Illness.objects.filter(illness_no=marker.illness_no)
                 for illness_item in illness:
                     nodes.append({'id': illness_item.illness_name, 'class': 'Molecule', 'group': 2, 'size': 15})
                     links.append({'source': marker.marker_name, 'target': illness_item.illness_name, 'value': 3})
        #组合成json字符串
        arg=json.dumps({'nodes': nodes, 'links': links})
        return render(request,'RecipeKG.html',{'arg':arg})
        # return HttpResponse(json.dumps({'nodes': nodes, 'links': links}))
def TargetKG(request,name):
        search_text=request.GET['search-TargetKG-text']
        if not search_text:
            return render(request, 'Targetindex.html')
        markers=Marker.objects.filter(marker_name=search_text)
        #搜索不到
        if not markers:
            return render(request, 'TargetKG.html', {'search_text':search_text})
        nodes = []
        links = []
        return render(request,'TargetKG.html')
def Search_herb(request,name):
    herb=MedMat.objects.filter(med_mat_name=name)
    return render(request, 'Search_herb.html', {'herb':herb[0]})