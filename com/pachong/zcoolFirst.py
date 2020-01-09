
import requests
from bs4 import BeautifulSoup
import csv
import json
## 从地址中获取图片
def getZcool(url):
    urlArray = []
    req=requests.get(url).text
    content=BeautifulSoup(req,'html.parser')
    comment_text = content.find_all('a',attrs={'class':'card-img-hover'})
    for image in comment_text:
        name=image.img['title']
        url=image.img['src']
        #  empty_dict=dict(zip([name],[url])) # 字典 {'wo':'我是src'}
        empty_dict=dict(zip(['name','src'],[name,url]))
        urlArray.append(empty_dict)  # list 列表添加
    return urlArray

if __name__ == '__main__':
    urlList=['https://www.zcool.com.cn/?p=2#tab_anchor']
    urlArray = getZcool(urlList[0])
    for i in urlArray:
        print(i)





