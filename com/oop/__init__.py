
##面对对象
class Student(object):
    def __init__(self,name,age,addr,parent):
        self.name=name
        self.age=age
        self.__addr=addr # private 无法被访问的
        self._parent=parent # 可以被访问

    def print_score(self):
        print('%s,%s'%(self.name,self.age))

    def set_addr(self,addr):
        self.addr=addr

bart=Student('nima',123)
bart.print_score()


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
class Animal(object):
    name='类属性< 实例的属性'
    def run(self):
        print('1')
class Dog(Animal):
     pass
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




