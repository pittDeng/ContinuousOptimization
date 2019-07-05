import random
from Func import setfunc
import numpy as np
def runiform(lowbound,highbound):
    return random.uniform(lowbound,highbound)
def takefitness(x):
    return x['pos'][-1]

C1=2.0
C2=2.0

class PSO:
    def __init__(self,**kwargs):
        self.dim_num=kwargs['dim_num']
        self.iter_num=kwargs['iter_num']
        self.pop_size=kwargs['pop_size']
        self.func=kwargs['func']
        self.bounds=kwargs['bounds']
        self.pop=[]
        self.gbest=[]
        self.invoke=0
        if(len(self.bounds)!=self.dim_num):
            raise RuntimeError('bounds矩阵的维数与dim_num不一致')
    def innerfunc(self,x):
        # self.invoke+=1
        # if(self.invoke>1e5):
        #     raise RuntimeError("超过调用次数")
        return self.func(x)
    def CheckExceed(self,x):
        for i in range(self.dim_num):
            if(x[i]<self.bounds[i][0] or x[i]>self.bounds[i][1]):
                x[i]=runiform(self.bounds[i][0],self.bounds[i][1])
        return x

    def __initilizeOne(self):
        '''
        这里倒数dim_num个为这个例子的搜过到的局部最优
        :return:
        '''
        item={'pos':[],
              'pbest':[],
              'v':[]
              }
        for i in range(self.dim_num):
            item['pos'].append(runiform(self.bounds[i][0],self.bounds[i][1]))
        item['pos'].append(self.innerfunc(item['pos']))
        item['pbest']=item['pos']
        for i in range(self.dim_num):
            item['v'].append(0.0)
        item['pos']=np.array(item['pos'])
        item['pbest']=np.array(item['pbest'])
        item['v']=np.array(item['v'])
        return item

    def __initilize(self):
        self.pop=[]
        for i in range(self.pop_size):
            self.pop.append(self.__initilizeOne())
        self.pop.sort(key=takefitness)
        self.gbest=self.pop[0]['pos']

    def __go(self):
        for i in range(self.iter_num):
            # weight=0.5*(i/self.iter_num)**2
            weight=0.0
            for j in range(self.pop_size):
                # weight=0.0
                # if(j<=0.2*self.pop_size):
                #     weight=0.5
                # else:
                #     # weight=0.0
                #     weight=0.5*(1-j/self.pop_size)
                # weight=0.5*(1-j/self.pop_size)
                for k in range(len(self.pop[j]['v'])):
                    self.pop[j]['v'][k]=weight*self.pop[j]['v'][k]+C1*runiform(0,1)*(self.pop[j]['pbest'][k]-self.pop[j]['pos'][k])+C2*runiform(0,1)*(self.gbest[k]-self.pop[j]['pos'][k])
                self.pop[j]['pos'][:-1]+=self.pop[j]['v']
                # if(self.isExceed(self.pop[j]['pos'][:-1])):
                #     self.pop[j]=self.__initilizeOne()
                self.pop[j]['pos'][:-1]=self.CheckExceed(self.pop[j]['pos'][:-1])
                self.pop[j]['pos'][-1]=self.innerfunc(self.pop[j]['pos'][:-1])
                if(self.pop[j]['pos'][-1]<self.pop[j]['pbest'][-1]):
                    self.pop[j]['pbest']=self.pop[j]['pos'].copy()
            self.pop.sort(key=takefitness)
            if(self.pop[0]['pos'][-1]<self.gbest[-1]):
                self.gbest =np.array(self.pop[0]['pos'])
            # if(self.dim_num>4):
            #     print('{}th best:'.format(i), self.gbest[-1])
            # else:
            #     print('{}th best:'.format(i), self.gbest)

    def run(self):
        self.__initilize()
        self.__go()

def testOnAFunction(func_name,dim_num):
    func=setfunc(func_name,dim_num=dim_num)
    from WWO import genBounds
    from Func import upbound
    maxbound=upbound(func_name)
    bounds=genBounds(-maxbound,maxbound,dim_num)
    pso=PSO(dim_num=dim_num,func=func,iter_num=2000,pop_size=50,bounds=bounds)
    pso.run()
    if (pso.dim_num > 4):
        print('{}th best:'.format(func_name), pso.gbest[-1])
    else:
        print('{}th best:'.format(func_name), pso.gbest)
    return pso.gbest[-1]

if __name__=='__main__':
    dim_num = 10
    from ToExcel import ToExcel
    toexcel=ToExcel("constantpsodata15.xls","data")
    # toexcel = ToExcel("psodata.xls", "data")
    for index in range(0,20):
        for name in range(1,21):
            res=testOnAFunction(name,dim_num)
            toexcel.insertData(name,index,res)
        print("{}time has been finished".format(index))
        toexcel.save()
    print('end')



