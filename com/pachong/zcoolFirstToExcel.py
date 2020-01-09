
import requests
from bs4 import BeautifulSoup



## 从地址中获取图片
def getZcool(url):
    urlArray = []
    req=requests.get(url).text
    content=BeautifulSoup(req,'html.parser')
    comment_text = content.find_all('a',attrs={'class':'card-img-hover'})
    for image in comment_text:
        name=image.img['title']
        url=image.img['src']
        urlItem=[]
        urlItem.append(name)
        urlItem.append(url)
        urlArray.append(urlItem)  # list 列表添加 list [ ['name','src'],[]]
    return urlArray

def toExcel(list1):
    output = open('D:\\Pictures\\data.xls','w',encoding='utf-8')
    output.write('name\tsrc\n')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            output.write(str(list1[i][j]))    #write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')   #相当于Tab一下，换一个单元格
        output.write('\n')       #写完一行立马换行
    output.close()



if __name__ == '__main__':
    urlList=['https://www.zcool.com.cn/?p=2#tab_anchor']
    urlArray = getZcool(urlList[0])
    print("------------")
    toExcel(urlArray)





