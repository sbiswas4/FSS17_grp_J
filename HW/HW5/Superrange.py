import os
import sys
import numpy as np

breaks = []
ranges = []
func = None

def get_permutations(low, high):
    x = []
    inc = 1 if low < high else -1
    if inc > 0:
        start = low
        end = high - 1
    else:
        start = low - 1
        end = high - 2
    while low != high:
        temp = []
        low += inc
        if inc > 0:
            end = low
        else:
            end -= inc
        for i in range(start, end, inc):
            temp.append(i)
        x.append(temp)
    #print x
    return x


def get_values(permute):
    global ranges

    x = []
    for i in permute:
        lst = [func(j) for j in ranges[i].terms]
        #print("lst",lst)
        x.extend(lst)


    return x

def combine(low, high, sup, bin):

    global ranges
    best = np.std(sup)

    cut = None
    #print("low",low,"high",high)
    lpermute = get_permutations(low, high)
    rpermute = get_permutations(high, low)

    for i in range(0, high-low-1):
        lvalues = get_values(lpermute[i])
        rvalues = get_values(rpermute[i+1])
        tmp_std = float(len(lvalues))/len(sup)*np.std(lvalues) + float(len(rvalues))/len(sup)*np.std(rvalues)
        if tmp_std < best:
            cut = i
            best = tmp_std
    if cut is not None:

        #print("bin",bin)

        bin = combine(low, cut + 1, lvalues, bin)
        bin = combine(cut + 1, high, rvalues, bin) + 1


    else:
        if len(breaks) <= bin:
            breaks.append(-float('Inf'))

        breaks[bin] = max(breaks[bin], ranges[high-1].high)
        #print("breaks bin",breaks[bin])
    return bin

def main(r, f):
    global ranges
    global func
    global breaks
    breaks = []
    ranges = r
    func = f
    # for index, value in enumerate(r):
    #     print "x, %d, %s" % (index + 1, value)
    #     print ("superrange",value.terms)

    length = len(ranges)
    original = get_values(range(0, length))




    combine (0, length, original, 0)
    return breaks