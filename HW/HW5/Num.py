import numpy as np

class c:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.hi = -1e32
        self.lo = 1e32
        self.w = 1
        self.independent_column = None
        self.elements = []
        self.variance = 0
    def __str__(self):
        return str(self.sd)

def create():
    return c()

def updates(t, f,name, all = c()):
    ll = len(t)
    all.n = 0
    y_all = []
    for _,one in enumerate(t):
        y = float(f(one))
        y_all.append(y)
        all = update(all,y)
    all.elements = t
    all.variance = np.var(y_all)
    all.independent_column = name
    return all

def update(i, x):
    i.n = i.n + 1
    if x < i.lo:
        i.lo = x
    if x > i.hi:
        i.hi = x
    delta = x - i.mu
    i.mu = i.mu + delta/i.n
    i.m2 = i.m2 + delta*(x-i.mu)
    if i.n > 1:
        i.sd = (i.m2/(i.n-1))**0.5
    #i.elements.append(x)
    return(i)