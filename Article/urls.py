from django.conf.urls import url
from .views import article_list,article_add

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
    url(r'^list/add/(?P<block_id>\d+)', article_add),
]

