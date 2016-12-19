from django.shortcuts import render

# Create your views here.

def article_list(request,block_id):
    block_id = int(block_id)
    #返回页面
    return render(request,"article_list.html")