## 时间模块
from datetime import datetime , timedelta

now=datetime.now()

dt=datetime(2015,4,19,12,20)
dt.timestamp()

## timestamp转化为 dateTime
t = 1429417200.0
print(datetime.fromtimestamp(t)) ## 这个就是本地时区的时间
# 转化为 格林威治就是
datetime.utcfromtimestamp(t)
## 相互转化
datetime.strptime('2019-25-00','%y%m%d')
now.strftime('%y%m%d')


now+timedelta(hours=10)



