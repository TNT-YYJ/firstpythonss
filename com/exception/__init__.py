## 处理异常
def foo():
    try:
        r=0
        if r==1:
            return -1
    except ZeroDivisionError as e:
        print('ex',e)
    finally:
        print('finally')
        




