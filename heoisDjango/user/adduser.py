# -*- coding: utf-8 -*-

from django.http import HttpResponse

from user.models import User


# 数据库操作
def add(request):
    test1 = User(username='cde',password='122')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")