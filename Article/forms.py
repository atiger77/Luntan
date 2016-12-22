#coding: utf-8
from django import forms
#添加校验器

class ArticleForm(forms.Form):
    art_title = forms.CharField(label="标题",max_length=100)
    content = forms.CharField(label="内容", max_length=10000)