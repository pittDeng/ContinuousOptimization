class PO:
    def __init__(self,**kwargs):
        self.dim_num=kwargs['dim_num']
        self.iter_num=kwargs['iter_num']
        self.pop_size=kwargs['pop_size']
        self.func=kwargs['func']
        self.bounds=kwargs['bounds']
        self.invoke_num=0
        try:
            self.invoke_num=kwargs['invoke_num']
        except(KeyError):
            self.invoke_num=1e5
        self.minimize=True
        try:
            self.minimize=kwargs['minimize']
        except(KeyError):
            self.minimize=True
        self.compare=None
        if(self.minimize):
            #如果要找最小值时就让第一个参数较第二个参数小时返回True
            self.compare=lambda x,y:True if x<y else False
        else:
            # 如果要找最小值时就让第一个参数较第二个参数小时返回False
            self.compare=lambda x,y:True if x>y else False
        self.pop=[]
        self.invoke = 0
        if(len(self.bounds)!=self.dim_num):
            raise RuntimeError('bounds矩阵的维数与dim_num不一致')

    def isExceed(self,x):
        for i in range(self.dim_num):
            if(x[i]<self.bounds[i][0] or x[i]>self.bounds[i][1]):
                return True
        return False

    def innerfunc(self,x):
        self.invoke+=1
        if(self.invoke>self.invoke_num):
            raise RuntimeError("调用超过允许次数")
        return self.func(x)