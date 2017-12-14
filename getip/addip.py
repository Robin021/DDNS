# -*- coding: utf-8 -*-
import json 
from django.http import HttpResponse
 
from ipapp.models import info
 
# 数据库操作
def addip(request):
    if request.method == 'POST':
        ip_json_data = json.loads(request.body)
        print (ip_json_data)
        ip = info(ip=ip_json_data['query'])
        ip.save()
        return HttpResponse("<p>done!</p>")
    else:
        # models.Tb1.objects.get(id=123)
        ip_result = info.objects.latest('ip')
	print (ip_result.ip)
        return HttpResponse(ip_result.ip)
