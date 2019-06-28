num=0
import math
def upbound(name):
    if name==1:
        return 5.12
    if name==2:
        return 10
    if name==4:
        return 1.28
    if name==5:
        return 30
    if name==8:
        return 10
    if name==11:
        return 1
    if name==12 or name==13:
        return 10
    if name==16:
        return 600
    if name==18 or name==19:
        return 5.12
    return 100

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
            # res=dec(0.0)
            res=0.0
            index=1
            for xi in x:
                res+=(10e6**((index-1)/(len(x)-1)))*xi*xi
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
    if name==11:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)):
                res+=(abs(x[i])**(i+2))
            return res
        return f
    if name==12:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)):
                res+=((i+1)*(x[i]**2))
            return res
        return f
    if name==13:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for xi in x:
                res+=(abs(xi*math.sin(xi)+0.1*xi))
            return res
        return f
    if name==14:
        def fbar(xi,yi):
            return (xi**2+yi**2)**0.25*(math.sin(50*(xi**2+yi**2)**0.1)**2+1)
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)-1):
                res+=fbar(x[i],x[i+1])
            res+=fbar(x[-1],x[0])
            return res
        return f
    if name==15:
        def fs(xi,yi):
            return 0.5+(math.sin((xi**2+yi**2)**0.5)**2-0.5)/(1+0.001*(xi**2+yi**2))**2
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)-1):
                res+=fs(x[i],x[i+1])
            res+=fs(x[-1],x[0])
            return res
        return f
    if name==16:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            temp=1
            for i in range(len(x)):
                res+=x[i]**2
                temp*=math.cos(x[i]/(i+1)**2)
            res=res/4000-temp+1
            return res
        return f
    if name==17:
        def tempf(xi,yi):
            return (0.5+(math.sin((100*xi**2+yi**2)**0.5)**2-0.5)/(1+0.001*(xi**2-2*xi*yi+yi)**2))**2
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for i in range(len(x)-1):
                res+=tempf(x[i],x[i+1])
            return res
        return f
    if name==18:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for xi in x:
                res+=(xi**2-10*math.cos(2*math.pi*xi)+10)
            return res
        return f
    if name==19:
        def tempf(xi):
            yi=0.0
            if(abs(xi)<0.5):
                yi=xi
            else:
                yi=round(2*xi)/2
            return yi**2-10*math.cos(2*math.pi*yi)+10
        def f(x):
            if (len(x) != dim_num):
                raise RuntimeError("输入数据的维数出错")
            res = 0.0
            for xi in x:
                res += tempf(xi)
            return res
        return f
    if name==20:
        def f(x):
            if(len(x)!=dim_num):
                raise RuntimeError("输入数据的维数出错")
            res=0.0
            for xi in x:
                res+=xi**2
            res=res**0.5
            res=1-math.cos(2*math.pi*res)+0.1*res
            return res
        return f









