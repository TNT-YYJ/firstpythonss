
import json

headersStr="""

accept:application/json, text/plain, */*
accept-encoding:gzip, deflate, br
accept-language:zh-CN,zh;q=0.9
authorization:bearer 3233f8fb-c3ce-470b-a045-aad07127033d

"""


def str_to_map(headers):
    headers = headers.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
    print(json.dumps(headers, indent=1))
    return headers


import requests
def toExcel(list1):
    output = open('D:\\Pictures\\data.xlsx','w',encoding='utf-8')
    # output.write('id\ttel\tname\n')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            output.write(str(list1[i][j]))    #write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')   #相当于Tab一下，换一个单元格
        output.write('\n')       #写完一行立马换行
    output.close()




if __name__ == '__main__':
    headers = str_to_map(headersStr)
    urlArray = []
    for i in range(1,22):
        fangurl = 'https://api.fangjinyun.com.cn/fjs/cronuscrm/api/v1/customerListNew?level=&page='+str(i)+'&size=2'
        mainStr=requests.get(fangurl,headers=headers)
        datastr=json.loads(mainStr.text).get('data')
        total=datastr.get('total')
        rows=datastr.get('rows')
        for row in rows:
            urlItem = []
            id=row.get('id')
            responseItemStr = requests.get("https://api.fangjinyun.com.cn/fjs/cronuscrm/api/v1/getTelePhone",
                                       params={'customerId': id}, headers=headers)
            tel = json.loads(responseItemStr.text).get('data')
            name=row.get('customerName')
            urlItem.append(name)
            urlItem.append(tel)
            urlArray.append(urlItem)
    toExcel(urlArray)




