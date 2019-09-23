###使用open直接打开文件，再使用read读取其中的内容，但是这样太麻烦
## 所以直接使用
with open('D:\\pricc.txt','r') as files:
    print(files.read())
# 这个with会自动调用 close()
## 由于这个read会一次性的读取所有的内容，很容易让把内存爆掉
#所以可以采用每次读取一行内容、
for line in files.readline():
    print(line.strip())

##读取二进制文件：图片 视频
f=open('/a.jpg','rb')
f=open('/a.txt','r',encoding='gbk')
# 如果是非法的编码字符，可以忽略
f=open('/a.txt','r',encoding='gbk',errors='ignore')

####----------写入------------------
with open('a.txt','w') as fwrite:  ## w模式就是直接覆盖， a模式是append
    fwrite.write('hello world')


####-------------在内存进行操作的stringIo--------------------------
from io import StringIO
stringIO=StringIO('tamengshuozhejiaoai')

### 调用系统的函数 使用os模块
import  os
os.environ.get('PATH')## 获取某个环境变量的值
##使用os进行路径的拆分和拼接
os.path.split('/user/a.txt')
os.path.join('/user','bin')
## 复制文件的
import shutil
##拿出所有的文件目录
list=[x for x in os.listdir('.') if os.path.isdir(x)]

## 序列化模式  json化
import pickle
d=dict(name='bob',age=123)
pickle.dumps(d)
import json
json.dumps(d)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
### 将对象实例进行json化
json.dumps(object,default=lambda obj:obj.__dict__)
## 反序列化时 也需要
json.loads(json_str,object_hook=dict2student)
#dict2student定义在 class类中的方法






















