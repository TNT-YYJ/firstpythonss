print('hello python ')

abc='''
字符串
'''
a=""
ab=''
abcd=9
# --------------------------------
list=[1,a,'cd',4,True,None]
list[0] #列表获取
list[1]=ab # 修改 ，可以重新赋值

tuple=(1,None,'cd') # 不准改其中元素
tuple[0] # 不能重新赋值

dic={'a':'1','b':'2'}
dic['a'] # 取值

# 集合自动去重
sset=set("asdf")
sset.remove('a')
fset=set("asdfasdfasdfhgfhgfjtg")
fbu=fset-sset
print(fbu)




