# -*- encoding: utf8 -*-
import requests
import re
import json
from urllib.parse import unquote
import shutil
from selenium import webdriver

youtube_adr = input("please input youtube address:")
s = requests.Session()
res = s.get(youtube_adr)
res.encoding = 'utf-8'
# print (res.text)
m = re.findall("ytplayer.config = ({.*?});",res.text)
jd = json.loads(m[0])
url_address = unquote(jd['args']['url_encoded_fmt_stream_map'])
urls = []
line = 0
line1 = 0
while(line != -1):
    try:
        line = url_address.find("url=",line+1)
    except:
        break;
    url = ""
    if(line == -1):
        url = url_address[line1+4:]
    elif(line != 0):
        url = url_address[line1+4:line]
    if(url.find("http") != -1):
        urls.append(url)
    line1 = line
    #print (line)
for u in urls:
    print(u)
req = s.get(urls[1],stream = True)
f = open('demo.mp4', 'wb')
shutil.copyfileobj(req.raw, f)
f.close
print ('finish!!')