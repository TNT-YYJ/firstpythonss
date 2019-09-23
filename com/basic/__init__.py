
not True # 就是非操作
None # # 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的

# 这里 静态语言在定义变量时必须指定变量类型，
a = 'ABC'
b = a
a = 'XYZ'
print(b)
#  将ABC指向了a    b也指向了ABC ， 这时a又被赋值， 但是b不变
10//3 # =3 的整数除法

str_a='asdf'
len(str_a) # 多少个字符

print('我是： %d  '% 2) # 格式化
print('我是： %s  '% 2) # 格式化
print('我是：{0} ---- %s  '.format('ren',2)) # 格式化

# -------------list------------------------
array=['1',1,3,True] # list一种有序的集合
array.clear()
array.append("asdf")
array[0]  # 注意索引别越界array[-1]
array.insert(1,'1-->insert')
array[2]='直接赋值'

#------------tupe-只是一串key而已-------------
t=(1,23)
t[0] # =1
tu=(1,[0,1])  # t[1][0]=0



#--------------------range 生成整数序列---------


#------dict-----------------------
# 就是相当于map
d={'a':'1','b':2}
d.get('a',1) # 取值根据key
d['a']
d=dict(zip([1,3,4],['a','b','c']))

#----------------------------------------
"""
  使用 str in 'hello str '
  copy 模块用来，深度复制 copy.copy()

"""
'asdf'.isalpha() # 是否只是含有字母
'asdf123'.isalnum() # 只是含有 字母和数字






