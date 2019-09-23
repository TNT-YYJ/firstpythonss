
import requests
requestss=requests.get("www.baidu.com",params={'token':'asdjfl23jljl'})
##  baidu.com?token=23423sdfsf

## post默认是 x-www-form-urlencoded
postreques=requests.post("www.baudmc.com",data={'formail':'ss@qq.com'})
postreques2=requests.post("www.baudmc.com",json={'formail':'ss@qq.com'})




