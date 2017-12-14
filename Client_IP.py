#-*- coding: UTF-8 -*-
import urllib3
import json
import time

def postIP(jsonData):

    http = urllib3.PoolManager()
    pjsonData = json.dumps(jsonData)
    s = http.request('POST', 'http://azure1.1more.cn:9092/ip/',
                     headers={'Content-Type': 'application/json'},
                     body=pjsonData)

    print(jsonData['query'])

def LastIP():
    file_object = open('ip.txt')

    try:
         all_the_text = file_object.read( )
    finally:
         file_object.close( )
    return all_the_text

def getIP():
    http = urllib3.PoolManager()
    r = http.request('Get','http://ip-api.com/json')
    jsonData = json.loads(r.data)
    return jsonData

def rewriteIP(newIP):
    file_object = open('ip.txt','w')

    try:
        file_object.write(newIP)
    finally:
        file_object.close( )

while 1:
    jsonData = getIP()
    postIP(jsonData)
    lastip = LastIP()
    if lastip == jsonData['query']:
        print(lastip)
    else:
        rewriteIP(jsonData['query'])
    time.sleep(3600)
