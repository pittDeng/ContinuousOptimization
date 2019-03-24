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