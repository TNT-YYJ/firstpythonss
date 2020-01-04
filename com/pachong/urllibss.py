
import urllib.request
import re
data=urllib.request.urlopen('http://www.baidu.com')
data1=urllib.request.urlretrieve('http://www.baidu.com','d.html') ## 直接下载在本地 ，图片下载的时候
## 测试
content=data.read()
data.getcode()
data.geturl()

# pat='<div class="name">(.*?)</div>'
# # rst=re.compile(pat).findall(data)
# # fh=open("a.txt",'w')
# # for i in range(0,len(rst)): ## 提取出的是 中文的 () 的文字
# #     print(rst[i])
# #     fh.write(rst[i]+'\n')
# # fh.close()

### urlopen  受url限制很大
for i in  range(1,2):
     try:
         file = urllib.request.urlopen('http://yum.iqianyue.com', timeout=44)
         print(file.read().decode('utf-8',"ignore"))
     except Exception as error:
         print('error : ',error)

### 模拟查询
keywd='Python'
keywd=urllib.request.quote(keywd)
urlbaidu="http://www.baidu.com/s?wd="+keywd+"&pn="+str(1)
patbaidu='Python(.*?)'
baidudata=urllib.request.urlopen(urlbaidu).read().decode('utf-8')
listbaidu=re.compile(patbaidu).findall(baidudata)
for i  in listbaidu:
    pass



