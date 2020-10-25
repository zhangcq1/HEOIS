# -*- coding: utf-8 -*-
from django.http import HttpResponse
from user.models import User
import json
# 数据库操作
def get(request):
    result = User.objects.all()
    print(result.values())
    return HttpResponse(json.dumps(list(result.values()), ensure_ascii=False), content_type="application/json,charset=utf-8")
