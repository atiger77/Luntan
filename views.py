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
    block_info = Block.objects.all().order_by("id")
    return render(request,"index.html",{"blocks":block_info})