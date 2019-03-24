from Func import setfunc
import random
def takelast(mylist):
    return mylist[-1]
class Jaya:
    def __init__(self,dim_num,popsize,iter_num,bounds,fitness_func):
        '''

        :param dim_num:
        :param popsize:
        :param iter_num:
        :param bounds: 必须满足[[lowbound1,highbounds1],[lowbound2,highbound2]]这种形式
        '''
        self.dim_num=dim_num
        self.popsize=popsize
        self.iter_num=iter_num
        self.bounds=bounds
        self.fitness_func=fitness_func
        self.pop=[]
        self.invoke=0

    def func(self,x):
        self.invoke+=1
        if(self.invoke>5e5):
            # 调用超过5e5次抛出异常，停止仿真
            raise RuntimeError("调用次数超过限制")
        return self.fitness_func(x)

    def initialize(self):
        self.pop=[]
        for i in range(self.popsize):
            item=Jaya.initilizeOne(self.dim_num,self.bounds)
            item.append(self.func(item))
            self.pop.append(item)
        self.pop.sort(key=takelast)

    @staticmethod
    def isExceed(x,bounds):
        for i in range(len(bounds)):
            if x[i]<bounds[i][0] or x[i]>bounds[i][1]:
                return True
        return False

    @staticmethod
    def initilizeOne(dim_num,bounds):
        item=[]
        for i in range(dim_num):
            item.append(random.uniform(bounds[i][0],bounds[i][1]))
        return item

    def run(self):
        self.initialize()
        for i in range(self.iter_num):
            for j in range(1,self.popsize-1):
                for k in range(self.dim_num):
                    self.pop[j][k]=self.pop[j][k]+random.uniform(0,1)*(
                            self.pop[0][k]-self.pop[j][k])-random.uniform(0,1)*(self.pop[-1][k]-self.pop[j][k])
                    if(Jaya.isExceed(self.pop[j][0:-1],self.bounds)):
                        self.pop[j][0:-1]=Jaya.initilizeOne(self.dim_num,self.bounds)
                    self.pop[j][-1]=self.func(self.pop[j][0:-1])
            self.pop.sort(key=takelast)
            print('{}th The Best value:'.format(i),self.pop[0][-1])



if __name__=='__main__':
    func,dim_num=setfunc("SumSquare")
    jaya=Jaya(dim_num,50,10000,[[-10,10],[-10,10]],func)
    jaya.run()
