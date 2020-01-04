##
import re
'''
  \w 任意一个字符或者 下划线
  \W 相反 
  \d  十进制数   \D  除了十进制的数 
  \s  空白字符
  
   . 除换行外的任意一个
   ^   $  开始结束
   * >=0   ?  0 or  1次 
   +  >=1 {n} n次
   {n,} >n   {n,m}  区间次
   | 或者
'''
strings="<a href='http://www.baidu.com'>百度</a>"
pat='[a-zA-Z]+://[^\s]*[.com|.cn]'
print(re.compile(pat).findall(strings))


