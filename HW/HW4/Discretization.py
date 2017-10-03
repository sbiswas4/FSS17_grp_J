import Range
import Superrange
import numpy as np
import tree
import csv
import Num.py

np.random.seed(1)

def nested_val(z):
    v = 2*np.random.rand()/100

    if z < 0.2:
        v += 0.2
    elif z < 0.6:
        v += 0.6
    else:
        v += 0.9
    return v


def x(z):
    return z[0]

def y(z):
    return z[1]


lst = list(np.random.rand(50))

for i, val in enumerate(lst):
    lst[i] = [val, nested_val(val)]
import csv
lst_dom = []
with open("auto_dom.csv","r") as inputFile:
        count = 0
        reader = csv.reader(inputFile,delimiter=",")
        included_columns = [5,8]
        for row in reader:
            count+=1
            if count ==1:
                continue
            content  = list(float(row[i]) for i in included_columns)
            lst_dom.append(content)


lst_dom = lst_dom[1:]
lst_dom = sorted(lst_dom)
print(lst_dom)
r = Range.main(lst_dom, x)

print "\nWe have many unsupervised ranges."
for index, value in enumerate(r):
    print "x, %d, %s" %(index + 1, value)
    print (value.terms)

print "=" * 60

print "\nWe have fewer supervised ranges."
breaks = Superrange.main(r, y)
for index, value in enumerate(breaks):
    print "super, %d, {label=%d, most=%f}" %(index, index, value)
print "\n"

# BINS OF HORSEPOWER

# sorted_lst_dom = sorted(lst_dom)
# tree_object = tree.Tree()
# result = tree_object.main(sorted_lst_dom)



master_list_horsepower = []
indexes = []
sorted_lst_dom = sorted(lst_dom)
dom_column = [element[0] for element in sorted_lst_dom]
for index,value in enumerate(breaks):
        if value in dom_column:
            i = max(loc for loc, val in enumerate(dom_column) if val == value)
        indexes.append(i)


horsepower_bin1 = sorted_lst_dom[:indexes[0]+1]
horsepower_bin1_dom = [element[1] for element in horsepower_bin1]
var1 = np.var(horsepower_bin1_dom)
print(horsepower_bin1)
horsepower_bin2 = sorted_lst_dom[indexes[0]+1:indexes[1]+1]
var2 = np.var(horsepower_bin2)
print("var2",var2)
horsepower_bin3 = sorted_lst_dom[indexes[1]+1:indexes[2]+1]
var3 = np.var(horsepower_bin3)
print("var3",var3)



