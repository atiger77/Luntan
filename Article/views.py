from django.shortcuts import render,redirect

from Article.models import Article
from Block.models import Block

#导入出现问题.记录下
# Create your views here.

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":article_objs,"b":block})

def article_add(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    '''
    if request.method == "GET":
        return render(request, "article_add.html", {"b": block})
    else:
        art_title = request.POST["art_title"].strip()
        art_content = request.POST["art_content"].strip()
        if not art_title or not art_content:
            return render(request, "article_add.html", {"b": block,"error":"标题或内容都不能为空!!","title":art_title,"content":art_content})
        if len(art_title) > 60 or len(art_content)>3000:
            return render(request, "article_add.html", {"b": block, "error": "标题或内容超出长度!!","title":art_title,"content":art_content})
        article = Article(block=block,title=art_title,content=art_content,status=0)
        article.save()
        return redirect("/article/list/%s"%block_id)
    '''
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = Article(block=block,title=form.cleaned_data["art_title"])

