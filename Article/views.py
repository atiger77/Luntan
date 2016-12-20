from django.shortcuts import render
from Block.models import Block
from Article.models import Article
# Create your views here.

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":article_objs,"b":block})

def article_add(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    return render(request,"article_add.html",{"b":block})