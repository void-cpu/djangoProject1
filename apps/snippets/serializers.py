# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 下午6:53
# @Author  : void bug
# @FileName: serializers.py
# @Software: PyCharm
from rest_framework import serializers

from apps.snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"
