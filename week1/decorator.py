from functools import wraps
from datetime import datetime

def log(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print("Function"+func.__name__+' has been called at '+datetime.now().strftime('%Y-%M-%d %H:%M:%S'))
        return func(*args,**kwargs)
    return decorator

@log
def add(x,y):
    return x+y

if __name__=='__main__':
    print("{},{}".format(add(2,3),add.__name__))
