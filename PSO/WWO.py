import random
import numpy as np
import copy
from PO import PO
from Func import setfunc

def runiform(lowbound,highbound):
    return random.uniform(lowbound,highbound)

def takefitness(x):
    return x['fitness']

def genBounds(low,high,dim_num):
    bounds=[]
    for i in range(dim_num):
        bound=[low,high]
        bounds.append(bound)
    return bounds

class WWO(PO):
    def __init__(self,alpha=1.001,beta=1,hmax=5,initlambda=0.5,**kwargs):
        PO.__init__(self,**kwargs)
        self.hmax=hmax
        self.initlambda=initlambda
        self.alpha=alpha
        self.beta=beta
        copybounds=np.array(self.bounds)
        copybounds=copybounds.transpose([1,0])
        self.L=copybounds[1]-copybounds[0]
        self.best=self.__initializeItem()
        self.worst=self.__initializeItem()
        self.kmax=self.dim_num

    def __initializeItem(self):
        item={
            'lambda':self.initlambda,
            'pos':[],
            'height':self.hmax,
            'fitness':0.0
        }
        return item

    def __initializeOne(self):
        item=self.__initializeItem()
        for i in range(self.dim_num):
            item['pos'].append(runiform(self.bounds[i][0],self.bounds[i][1]))
        item['fitness']=self.innerfunc(item['pos'])
        return item

    def __initialize(self):
        for i in range(self.pop_size):
            self.pop.append(self.__initializeOne())
        self.pop.sort(key=takefitness,reverse=not self.minimize)
        self.best=self.pop[0]
        self.worst=self.pop[-1]

    def __propagation(self,item):
        newitem=copy.deepcopy(item)
        for i in range(self.dim_num):
            newitem['pos'][i]+=(runiform(-1,1)*newitem['lambda']*self.L[i])
            if(newitem['pos'][i]<self.bounds[i][0]or newitem['pos'][i]>self.bounds[i][1]):
                newitem['pos'][i]=runiform(self.bounds[i][0],self.bounds[i][1])
        newitem['fitness']=self.innerfunc(newitem['pos'])
        if(self.compare(newitem['fitness'],item['fitness'])):
            item=newitem
            if(self.compare(newitem['fitness'],self.best['fitness'])):
                item=self.__breaking(item)
        else:
            item['height']-=1
            if(item['height']==0):
                item=self.__refraction(item)
        item['lambda'] *= (self.alpha ** (-(1/item['fitness'] - 1/self.worst['fitness'] + 1e-9) / (
                1/self.best['fitness'] - 1/self.worst['fitness'] + 1e-9
        )))
        return item

    def __refraction(self,item):
        item=copy.deepcopy(item)
        fitness=item['fitness']
        for i in range(self.dim_num):
            item['pos'][i]=random.gauss(mu=(item['pos'][i]+self.best['pos'][i])/2,sigma=abs(item['pos'][i]-self.best['pos'][i])/2)
            while(item['pos'][i]<self.bounds[i][0] or item['pos'][i]>self.bounds[i][1]):
                item['pos'][i] = random.gauss(mu=(item['pos'][i] + self.best['pos'][i]) / 2,
                                              sigma=abs(item['pos'][i] - self.best['pos'][i]) / 2)
        item['fitness']=self.innerfunc(item['pos'])
        item['height']=self.hmax
        item['lambda']*=(item['fitness']/fitness)
        return item

    def __breaking(self,item):
        breaking=copy.deepcopy(item)
        selected_dims=[]
        for i in range(random.randint(0,self.kmax)):
            selected_dims.append(random.randint(0,self.dim_num-1))
        for s_dim in selected_dims:
            newitem=copy.deepcopy(item)
            newitem['pos'][s_dim]+=random.gauss(mu=0,sigma=1)*self.beta*self.L[s_dim]
            while(newitem['pos'][s_dim]<self.bounds[s_dim][0] or newitem['pos'][s_dim]>self.bounds[s_dim][1]):
                newitem = copy.deepcopy(item)
                newitem['pos'][s_dim] += random.gauss(mu=0, sigma=1) * self.beta * self.L[s_dim]
            newitem['fitness']=self.innerfunc(newitem['pos'])
            if(self.compare(newitem['fitness'],breaking['fitness'])):
                breaking=newitem
        return breaking

    def __go(self):
        for i in range(self.iter_num):
            for j in range(self.pop_size):
                self.pop[j]=self.__propagation(self.pop[j])
            self.pop.sort(key=takefitness,reverse=not self.minimize)
            self.best=self.pop[0]
            self.worst=self.pop[-1]
            if(self.dim_num<4):
                print('{}th best value'.format(i), self.best['pos'], self.best['fitness'])
            else:
                print('{}th best value'.format(i), self.best['fitness'])


    def run(self):
        self.__initialize()
        self.__go()


if __name__=='__main__':
    dim_num=30
    func=setfunc('sincos',dim_num=dim_num)
    bounds=genBounds(-100,100,dim_num)
    wwo=WWO(func=func,dim_num=dim_num,iter_num=300,pop_size=50,bounds=bounds)
    wwo.run()
    print('end')
