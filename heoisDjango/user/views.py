from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
def login(request):
    result = {"status": "错误", "data": "", "city": "北京"}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")