from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from Article.models import Article
from Block.models import Block
from Article.forms import ArticleForm


def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    '''实现分页器功能'''
    article_cnt_1page = 3
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles, article_cnt_1page)
    page = p.page(page_no)
    article_objs = page.object_list

    return render(request,"article_list.html",{"articles":article_objs,"b":block,"page":page})

def article_add(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)

    if request.method == "GET":
        return render(request, "article_add.html", {"b": block})
    else:
        '''
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
            article = Article(block=block,title=form.cleaned_data["art_title"],content=form.cleaned_data["art_content"],status=0)
            article.save()
            return redirect("/article/list/%s" % block_id)

        else:
            return render(request,"article_add.html",{"b":block,"form":form})
