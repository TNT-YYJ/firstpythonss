
"""
https://juejin.im/timeline


"""

import requests
from bs4 import BeautifulSoup
import json

headerstr="""
Cache-Control:max-age=0
Connection:keep-alive
Cookie:pgv_pvid=1899203480; pgv_pvi=8412132352; __guid=166713058.1145804318062056000.1564989668174.8127; rewardsn=; wxtokenkey=777; monitor_count=1
Host:mp.weixin.qq.com
"""

def str_to_map(headers):
    headers = headers.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
    return headers

url='https://mp.weixin.qq.com/s/3HaYLVHxRYmIfd3vYJIQbg'

import logging
if __name__ == '__main__':
    # requestText=requests.get(url,headers=str_to_map(headerstr)).text
    requestText=requests.get(url).text
    imglist=[]
    soupDocu=BeautifulSoup(requestText,'html.parser')
    plist=soupDocu.select("p > img")
    for p in plist:
        url =''
        try:
            url=p['data-src']
            logging.info('日志功能')
            assert url==None,'不能为null'
        except Exception as e : # 异常的捕获
            url=None
        finally:
            imglist.append(url)
# python -O err.py 启动的时候 使用-o 来关闭 assert

## 单元测试
import unittest
import com.oop.mixln ## 和java一样

## unittest.TestCase 这个就是测试的标记
class TestUnit(unittest.TestCase):
    def test_init(self): # test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d= com.oop.mixln.Dogs() ## 对象名字也需要root package的名字
        self.assertEqual(d,1)
        # 期待抛出异常 通过__getattribute__(self,'value')访问不存在的key时，断言会抛出AttributeError：
        with self.assertRaises(AttributeError):
            value=d.__getattribute__(self,'value')

## 在方法最后加上 测试类的
if __name__ == '__main__':
    unittest.main()

## 如果需要在调用的方法的前后增加 init 和 destroy方法
## 可以使用 setUp setDown 比如：链接数据库 和释放链接


