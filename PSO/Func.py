num=0
import math
def setfunc(name,dim_num):
    if name=='sphere':
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)):
                res+=((i+1)*x[i]**2)
            return res
        return f
    if name=='sincos':
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            sumsquare=0
            for xi in x:
                sumsquare+=xi**2
            sumsquare=sumsquare**0.5
            return 1-math.cos(2*math.pi*sumsquare)+0.1*sumsquare
        return f