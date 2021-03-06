# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xmltodict
from django.shortcuts import render
from django.http import HttpResponse
import redis
from django.views.decorators.csrf import csrf_exempt

g_redis=redis.StrictRedis(host='localhost', port=6379, db=0)

@csrf_exempt
def index(request):
    response='<mt-sms-smpp-response version="1.0" id="%d"><status>%s</status></mt-sms-smpp-response>'    
    try:
        d = xmltodict.parse(request.body)
    except Exception:
        response=response%(0,"Error")
        return HttpResponse(response)

    property_id=int(d['mt-sms-smpp-request']['@id'])
    response=response%(property_id,"success")
    print response

    return HttpResponse(response)



