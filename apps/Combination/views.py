from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Max
from apps.Graphapp.models import Formulas,Forcom
import uuid
import json

# Create your views here.

#加减化裁界面
def FCom(request,name):
    recipe=Formulas.objects.filter(formulas_name=name)
    reccoms=Forcom.objects.filter(formulas_no=recipe[0].formulas_no).values_list('herbs_name',flat=True)
    if request.POST.get("save") == "add":
        try:
            #计算新方剂编号
            #marker=2:自建方剂
            formulas_name=request.POST.get("formulas_name")
            formulas_no=uuid.uuid5(uuid.NAMESPACE_DNS, formulas_name)
            print(formulas_no)
            count = Formulas.objects.filter(formulas_name=formulas_name).count()
            arg=json.dumps({'name': count})
            if count>0:
                return render(request, 'FCom.html', {'reccoms':reccoms, 'recipe':recipe[0],'arg':arg})
            Formulas.objects.create(
                        formulas_no=formulas_no,
                        formulas_name=formulas_name,
                        mark=2,
                    )
            for i in range(1,len(request.POST)-2):
                i=str(i)
                print(request.POST.get(i))
                if request.POST.get(i):
                    herbs_name=request.POST.get(i)
                    forcom_no=uuid.uuid5(uuid.NAMESPACE_DNS, herbs_name)
                    print(forcom_no)
                    Forcom.objects.create(
                              forcom_no=forcom_no,
                              formulas_no=formulas_no,
                              herbs_name=request.POST.get(i),
                              mark=2,
                          )
            message = "操作成功！"
        except Exception as e:
            print(str(e))
            message = "操作失败:请尝试重新填写！"
        return render(request, 'FCom.html', {'reccoms':reccoms, 'recipe':recipe[0],'message':message,'arg':arg})
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


