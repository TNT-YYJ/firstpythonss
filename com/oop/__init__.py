#------------------------------------------------------------------
##面对对象
class Student(object):
    def __init__(self,name,age,addr,parent):
        self.name=name
        self.age=age
        self.__addr=addr # private= __ 无法被访问的
        self._parent=parent # 可以被访问

    def print_score(self):
        print('%s,%s'%(self.name,self.age))

    def set_addr(self,addr):  # 方法 动态的特征
        self.addr=addr

bart=Student('nima',123)
bart.print_score()
print(bart._parent)

bart2=Student()
bart2.name='qingcnag'

##
bart = Student('Bart Simpson', 59)
bart.get_name()
'Bart Simpson'
bart.__name = 'New Name' # 设置__name变量！ 在外部申明的 __name 和本身的_name 是两个概念，
bart.__name
'New Name'
## 内部的_ _name变量已经被Python解释器自动改成了_Student_ _name，
# 而外部代码给bart新增了一个_ _name变量。不信试试：
# 继承

#------------------------------------------------------------------
# 定义类里面的属性 self.myname
class teacher:
    def __init__(self,name,job):
        self.myname=name
        self.myjob=job

c=teacher('我','老师')
print(c.myjob)
#------------------------------------------------------------------
#通过对象调用方法
class cla2:
    def myfunc1(self,name):
        print('hello'+name)
cd=cla2()
cd.myfunc1('weiwei')

#------------------------------------------------------------------
#通过对象调用方法调用 自定义属性
class cla3:
    def __init__(self, name, job):
        self.myname = name
        self.myjob = job
    def myfunc1(self):
        print('hello'+self.myname)

cf=cla3('名字','工作')
cf.myfunc1()

#------------------------------------------------------------------
#通过对象调 继承重载
#重载:在子类中对父类继承过来的特征重新定义

class parent:
    def talk(self):
        print('talking')
class mother:
    def cook(self):
        print('cooking')
class sonModel(parent):  # 继承 子类(父类)
    pass
class sisterModel(parent,mother):## 多继承
    def lister(self):
        print('listening')
    def talk(self):
        print('重载 talk ')
class son2Model:
    pass

son1=sonModel()
son1.talk()

sister1=sisterModel()
sister1.talk()
sister1.cook()






class Animal(object):
    name='类属性< 实例的属性'
    def run(self):
        print('1')
class Dog(Animal):
    def run_twice(animal):
        animal.run()

hasattr(Dog(),'name')


## 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性
# ，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
from  types import MethodType
class mans(object):
    __slots=('name','age') ## 这个就是对属性进行限制的写法，但是对 继承者不做作用
man1=mans()
man1.name='m名字'
man1.score='65'

class God(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
           raise ValueError('有错') ## 主动的抛出错误
        if value>10:
            raise ValueError('不行')
        self._score=value

s = God()
s.set_score(60) # ok!
s.get_score()
s.set_score(9999)

## 用注解标识出属性
class TwoGog(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
           raise ValueError('有错') ## 主动的抛出错误
        if value>10:
            raise ValueError('不行')
        self._score=value
ss=TwoGog()
s.score=22 # 这样就是直接赋值了




