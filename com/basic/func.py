
import math

# 返回多个值的函数
def funct1():
    return 1,23
x,y=funct1()

if funct1()!=(1,23):
    print('nima')
else:print("wocao")

# 默认参数 最好别用 list当默认参数
def funct2(x,n=2):
    print('默认参数放后面')

## 可变参数
def fiunc3(*num):
    sum=1
    for x in num:
        sum=x+sum
fiunc3([1,3,4]) # list
fiunc3((1,3,4)) # tuple

## 命名关键字参数，限制传入的 参数的名字
def namefunct3(name,*,age):
    print(name,age=2)



## 关键字参数   可以将多余信息也传入
def keyfunction(x,**kwargs):
    print('x',x,'ke',kwargs)
extra = {'city': 'Beijing', 'job': 'Engineer'}
## **extra 表示将所有的数据全部传入 **kwargs 里面，并且传入的是一份拷贝
keyfunction('Jack', 24, **extra)

## 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

 # *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
