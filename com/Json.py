
import json

headers="""

accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
cookie:JSESSIONID=aaaVeC1FyBjoyhaAXDcXw; __guid=72146453.3532339548224043000.1564639434212.2427; up_location_prompt=1; gr_user_id=19f1d960-9bcb-44e1-85a4-b7e2dcf23b5b; zid=1564639485xfuz; nav_tab_home=1; zcool_logon_new=19325878%7C%7C%7Cnull%7C%7Cnull%7C20190801140838%7C02D3E2489DAC0FA276131C8572EDC097; zcool_logon_hw=19325878%7C%25E5%25B0%258F%25E6%2599%25BA_0x01%7Chttps%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F1noavatar.gif%7C17316311937%7C20190801140838%7CF5777E10F0FDEE50218F5CA9193F6139; zui=%7B%22memberType%22:0,%22memberProfession%22:%22%E8%AE%BE%E8%AE%A1%E7%88%B1%E5%A5%BD%E8%80%85%22,%22memberRecommender%22:%22%E6%9C%AA%E6%8E%A8%E8%8D%90%22,%22memberGender%22:%22%E7%94%B7%22,%22pageUrl%22:%22https://www.zcool.com.cn/u/19325878%22,%22username%22:%22%E5%B0%8F%E6%99%BA_0x01%22,%22avatar%22:%22https://static.zcool.cn/git_z/z/images/boy.png%22,%22id%22:19325878%7D; activeDay=contentId%3D6696419_3%26day%3D2019-08-01; gr_cs1_c27544cf-5c4c-4038-8116-2fc3ebfd6743=uid%3A19325878; monitor_count=15
referer:https://www.zcool.com.cn/work/ZMzgxMjU2MjQ=.html
upgrade-insecure-requests:1
user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

"""


def str_to_map(headers):
    headers = headers.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
    print(json.dumps(headers, indent=1))
    return headers


#if __name__ == '__main__':
    #print("start")
    #ma_comment = str_to_map(headers)
    #print(ma_comment)


strin='https://img.zcool.cn/community/0106495cbd3de7a80121416806ccf0.jpg@1280w_1l_2o_100sh.jpg'
strArray=strin.split("/")[-1].split('@')[0].split('.')[0]
print(strArray)


#传入可迭代对象  建立字典 map
b = dict(zip(['one','two','three'],[1,2,3]))
print(b)

# 集合的使用
aCollection= set(('a','csdf','d'))
bv= {x for x in 'asdfasdf'}
# 移除
#aCollection.remore('a')
#aCollection.discard('a')
#aCollection.clear()

# 列表
alist=['a','b','c']
#del alist[0]
#'a' in alist


## 字典
dictA=dict(zip(['name','src'],['网二','www.baidu.com']))
dictAb={'name':'nimade'}
#del dictA['Name']
#dictA.get('name') # dictA.get（1,0）返回值是0；

