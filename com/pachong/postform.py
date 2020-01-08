import urllib.request,re,json
import urllib.parse

posturl='http://www.iqianyue.com/mypost'
postdata=urllib.parse.urlencode({
    'name':'',
    'pass':''
}).encode('utf-8')
req=urllib.request.Request(posturl,postdata)
### 模拟浏览器访问
## 就是加个头而已
url='http://blog.csdn.net'
headers=("User-agent","Mozilla/5.0")
opener=urllib.request.build_opener()
opener.addhanders=[headers]
data=opener.open(url).read()
fh=open('x.txt','wb')
fh.write(data)
fh.close()






