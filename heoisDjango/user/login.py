# -*- coding: utf-8 -*-
from django.http import HttpResponse
from user.models import User
import json
# 数据库操作
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        try:
            result = User.objects.get(username = username,password=password)
        except:
            result = 0
        print(result)
        if result:
            return HttpResponse(json.dumps({'state':True}, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(json.dumps({'state': False}, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        result = User.objects.get(username = username,password=password)
        if result:
            return HttpResponse(json.dumps({'state':True}, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(json.dumps({'state': False}, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")