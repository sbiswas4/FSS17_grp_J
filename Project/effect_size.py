'''
Created on 21-Nov-2017

@author: advai
'''
from statistics import mean, stdev
from math import sqrt

# test conditions
# c0 = [0.924,0.917,0.933,0.923,0.926]
# c0 =  [0.921,0.917, 0.920, 0.921, 0.922]
c0=[0.919,0.916,0.922,0.923,0.920]


# c1=[0.896]*5 
# c1=[0.897]*5
c1=[0.899]*5
 
# c0 = []
# c1 = [i * 2 for i in c0]

cohens_d = (mean(c0) - mean(c1)) / (sqrt((stdev(c0) ** 2 + stdev(c1) ** 2) / 2))

print(cohens_d)