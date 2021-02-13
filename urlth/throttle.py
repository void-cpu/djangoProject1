# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 下午9:31
# @Author  : void bug
# @FileName: throttle.py
# @Software: PyCharm
from rest_framework.throttling import SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):
    scope = "anonymous"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    scope = "user"

    def get_cache_key(self, request, view):
        return request.user.username
