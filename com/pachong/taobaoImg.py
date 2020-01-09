
import urllib.request
import re
import random
imgurl='https://www.homedo.com/act/sdqianggou.shtml'

pat='<img src="(.*?)"'
data=urllib.request.urlopen(imgurl).read().decode('utf-8','ignore')
imagurls=re.compile(pat).findall(data)
for i in imagurls:
    localfile="E:\\pythonTest\\"
    imageurlfile=None
    if not i.startswith('https:'):
        imageurlfile='https:'+i
    else:
        imageurlfile=i
    urllib.request.urlretrieve(imageurlfile,filename=localfile)
### urllib 太弱智



