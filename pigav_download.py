import requests 
import re
import shutil
    
res = requests.get(input("輸入朱古力要下載的影片網址："))
dis = re.findall('(https://v[0-9].?.wuso.tv/wp-content/uploads/.*.mp4)',res.text)
print (dis[0])
res = requests.get(dis[0],stream = True)
print(dis[0].split('/')[-1])
f = open(dis[0].split('/')[-1], 'wb')
# 開啟新增一檔案 
shutil.copyfileobj(res.raw, f)
# 儲存擷取的串流  
f.close
# 關閉串流
print ('finish!!')