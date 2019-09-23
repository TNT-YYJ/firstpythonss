class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
## 多重继承，mixln ：还需要添加其他的功能
class Dog(Runnable,Flyable):
      pass

class Dogs():
    pass
## 枚举类
from  enum import Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Sun2=20
    Sun23=40
    Sun4=50

Month=Enum('Month',('Jun','Oct'))
day1=Weekday.Sun
day2=Weekday['Oct']
day1.value
Month(1)

## 魔术代码  给类动态的增加方法的  meteclass  给自定义的mylist增加add方法
## metaclass是类的模板
class ListMeta(type):
    def __new__(cls, name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)


class mylist(list,metaclass=ListMeta):
       pass
##  -----------常用在 orm的映射中-----







