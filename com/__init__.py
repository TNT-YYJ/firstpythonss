import urllib
import requests
import json
from bs4 import BeautifulSoup
import re

headerStr="""

accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
cookie:JSESSIONID=aaaVeC1FyBjoyhaAXDcXw; __guid=72146453.3532339548224043000.1564639434212.2427; up_location_prompt=1; gr_user_id=19f1d960-9bcb-44e1-85a4-b7e2dcf23b5b; zid=1564639485xfuz; nav_tab_home=1; activeDay=contentId%3D6696419_3%26day%3D2019-08-01; gr_cs1_ee52f055-e3eb-4f87-80f3-e1c3fd1a7e50=uid%3A19325878; gr_session_id_acec0eb2dafeaf05=9c51b20d-1ff6-408b-b6ae-d680bb8ef416; gr_cs1_9c51b20d-1ff6-408b-b6ae-d680bb8ef416=uid%3A0; gr_session_id_acec0eb2dafeaf05_9c51b20d-1ff6-408b-b6ae-d680bb8ef416=true; monitor_count=19
referer:https://www.zcool.com.cn/work/ZMzgxMjU2MjQ=.html
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
"""

def str_to_map(headers):
    headers = headers.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
    return headers
Headers=str_to_map(headerStr)
## 从地址中获取图片
def getZcool():
    urlArray = []
    url='https://www.zcool.com.cn/work/ZMzUyMjgyMDA=.html'
    req=requests.get(url).text
    content=BeautifulSoup(req,'html.parser')
    comment_text = content.find_all('img', attrs={'class': 'no-right-key'})
    for image in comment_text:
        print(image)
        # <img class="no-right-key" data-height="2250.0" data-info="绘画小能手渣熊对此作品设置了隐私保护，禁止保存至本地。" data-width="3000" src="https://img.zcool.cn/community/0155855cbd3de3a801214168b9988e.jpg@1280w_1l_2o_100sh.jpg"/>
        url=image.get('src')
        if(isIllgal(url)):
            urlArray.append(url)
    return urlArray
## 根据url下载到本地
def download_img(img_url,nameType):
    r = requests.get(img_url,stream=True)
    print(r.status_code)
    imageName = img_url.split("/")[-1].split('@')[0].split('.')[0]
    if r.status_code == 200:
        open('D:\\Pictures\\img_'+imageName+'.png', 'wb').write(r.content) # 将内容写入图片
        print("下载完成")
    del r

## 匹配条件
def isIllgal(url):
    print(url)
    if(url!=None):
        # 以什么结尾
        pattern = '.+\.(jpg|img)$'
        print('--------' + url)
        m = re.match(pattern, url)
        if(m!=None):
            return True
    else:
        return False

if __name__ == '__main__':
    urlArray = getZcool()
    for i in range(len(urlArray)):
        download_img(urlArray[i],str(i))
