from django.http import HttpResponse
from django.shortcuts import render
from Block.models import Block

def index(request):
    '''
    block_info = [
        {"name": "业务安全板块", "desc": "分享业务安全知识", "manager": "atiger77"},
        {"name": "运维安全板块", "desc": "分享运维安全知识", "manager": "atiger77"},
        {"name": "应用安全板块", "desc": "分享应用安全知识", "manager": "atiger77"}
    ]
    '''
    #只展示状态为正常的板块, Block中models.py定义。
    #block_info = Block.objects.all().order_by("id")
    block_info = Block.objects.filter(status=0).order_by("id")
    return render(request,"index.html",{"blocks":block_info})