num=0
import math
def setfunc(name):
    if name=='sphere':
        def f(x):
            if(len(x)!=2):
                raise RuntimeError("输入数据的维数出错")
            return x[0]**2+x[1]**2
        return f,2
    if name=='SumSquare':
        def f(x):
            if(len(x)!=2):
                raise RuntimeError("输入数据的维数出错")
            return x[0]**2+2*x[1]**2+2
        return f,2
    if name=='sincos':
        def f(x):
            if(len(x)!=3):
                raise RuntimeError("输入数据的维数出错")
            return math.cos(math.sin(x[0]))**2+math.sin(math.cos(x[0]+x[1]+x[2]))
        return f,3