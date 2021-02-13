# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 下午7:00
# @Author  : void bug
# @FileName: urls.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter

from apps.snippets.views import SnippetViewSet

routers = DefaultRouter()
routers.register('Snippet', SnippetViewSet)

