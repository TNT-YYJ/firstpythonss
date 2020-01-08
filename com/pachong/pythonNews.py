## 新闻爬虫
##  需求： 将腾讯新闻首页的所有的新闻爬到本地上
###  思路： 首页爬取，通过正则表达式获取所有的链接，保存到本地
import urllib.request
import re

url='https://news.qq.com/'
sigleurl='https://new.qq.com/omn/SJD20200/SJD2020010601804000.html'
data=urllib.request.urlopen(url).read().decode('GB2312','ignore')
pat='href="(.*?)"'
alllink=re.compile(pat).findall(data)
for i in alllink:
    pass
#### 用户代理池 ： 构建之后，随机的调用
import random
agentPool=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

]

def ua(agentPool):
    ag= random.choice(agentPool)
    headers=("User-agent",ag)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

##ip 代理池 西刺
###
ip='localhost:808'
proxy=urllib.request.ProxyHandler({'http':ip})
openders=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(openders)
data=urllib.request.urlopen(url).read().decode('GB2312','ignore')

###接口调用的方式


