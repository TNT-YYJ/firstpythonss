import re

## eg
string='taoyunjiaoyu'
pat='yun'
rslt=re.search(pat,string)## 普通字符作为原子
print(rslt)

## 非打印字符作为原子 \n \t
string2='''
 aas234234df
 asdf
'''
pat2='\n'
rlst2=re.search(pat2,string2)

##通用字符做为原子
'''
  \w 任意一个字符或者 下划线
  \W 相反 
  \d  十进制数   \D  除了十进制的数 
  \s  空白字符
'''
pat3='\w\d'
rsl23=re.search(pat3, string2)


## 原子表  从中任意选择一个
pat4='asdf[xys]hkk'
pat4='asdf[^xys]hkk'  ## 非^

### 元字符 重复几个数字
'''
   . 除换行外的任意一个
   ^   $  开始结束
   * >=0 
   ?  0 or  1次 
   +  >=1
   {n} n次
   {n,} >n 
   {n,m}  区间次
   | 或者
'''

string5='tayun23422342kljlj'
pat='ta.u'
pat='^a'
pat='l.$'
patz='2{2,}'
print(re.search(patz,string5))

##-----------------------
'''
 模式修正符
 I 忽略大小写 
 L M 
 U unicode 
 S 让.匹配包括换行符
'''
s=re.search('df','asdf',re.I)

##贪婪模式  懒惰模式
part1='p.*y'
part1='p.*?y' # 精准，找到就停

###  search 是任意一个地方
# match 是 从头开始匹配
# 全局匹配：
Strings='pxysdply22pyy'
pat6='p.*?y'
print(re.compile(pat6).findall(Strings)) ## 找到所有的
### 正则表达式函数




















