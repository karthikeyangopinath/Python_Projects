# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:37:55 2021

@author: karthik
"""

import numpy as np
from numpy import linalg as LA

Inp=[]
no_features=int(input('Enter the number of features: '))
no_instances=int(input('Enter the number of instances: '))
print('Enter the data with enter:')
for i in range(0, no_features*no_instances):
    ele = int(input())
    Inp.append(ele) # adding the element    
print(Inp)


xT=np.array(Inp)
xT=xT.reshape(no_instances,1,no_features,)


print(xT)
a=[]
for i in range(no_instances):
    for j in range(no_instances):
        a.append(np.sqrt(np.sum(np.power(xT[i]-xT[j],2))))
a=np.array(a)
a=a.reshape(no_instances,no_instances)
print(a)        
        
        
