from collections import Iterable
d={'a':1,'sdf':2}
for x in d:
    print(x)

for x in d.values():
    print(x)

## 判断是否是一个可以迭代的对象
isinstance('asdf',Iterable)
## 循环list的下标
for i,value in enumerate([1,3,4,5]):
    print(i,value)

## 循环的间写
xd=[x * x for x in range(1, 11) if x % 2 == 0]

ks=[m+j for m in 'asdf'  for j in 'hfg']

# 类似的 lambda的表达式的内置函数

## reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,3,4,4])
# = 12


def f(x):
    return x*2
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
r=list(map(f,[1,3,4,5]))
list(r) # = 2,6,8,10


# 忽略大小写进行排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)


## 函数内部定义函数
def waibu(*args):
    def sum():
        return 1
    return sum
f=waibu([1,3,4,5])

## 匿名函数
nums=map(lambda x : x*x ,[1,3,4,5])
lambda x:x+x # 相当于
def f(x):
    return x+x

ff=lambda x:x+x
ff(5) # =10 这就是调用方式

## 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator 自定义的aop
def log(func):
    def wrapper(*args,**kwargs):
        print('asdf')
        return func(*args,**kwargs)
    return wrapper

@log
def nowTime():
    print('time')


## 简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
import functools
int2=functools.partial(int ,base=2)
int2('10001010')

__xx=2# private的




