num=0
import math
def setfunc(name,dim_num):
    if name==1:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)):
                res+=((i+1)*x[i]**2)
            return res
        return f
    if name==2:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            sumsquare=0
            for xi in x:
                sumsquare+=xi**2
            sumsquare=sumsquare**0.5
            return 1-math.cos(2*math.pi*sumsquare)+0.1*sumsquare
        return f
    if name==3:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            index=1
            for xi in x:
                res+=((10e6)**((index-1)*xi*xi/(len(x)-1)))
                index+=1
            return res
        return f
    if name==4:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0
            index=1
            # 这里要不要加rand()
            for xi in x:
                res+=(index*(xi**4))
            return res
        return f
    if name==5:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for index in range(0,len(x)-1):
                res+=(100*(x[index+1]-x[index]**2)**2+(x[index]-1)**2)
            return res
        return f
    if name==6:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0

            for i in range(1,len(x)):
                temp=0.0
                for j in range(0,i):
                    temp+=x[j]
                res+=(temp)**2
            return res
        return f
    if name==7:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(1,len(x)):
                res=max(abs(x[i]),res)
            return res
        return f
    if name==8:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            temp=1.0
            for xi in x:
                res+=abs(xi)
                temp*=abs(xi)
            return res+temp
        return f
    if name==9:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for xi in x:
                res+=(xi**2)
            return res
        return f
    if name==10:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for xi in x:
                res+=((xi+0.5)**2)
            return res
        return f

