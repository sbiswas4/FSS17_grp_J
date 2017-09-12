import os
import sys
import reading_csv

class Header:
    def __init__(self):
        self.name = []
        self.ignore = []
        self.num = []
        self.goal = []
        self.sym = []

    def __str__(self):
        return str(self.name)

class Row:
    def __init__(self):
        self.content = []
        self.rank = -1
        self.index = -1

    def __str__(self):
        return "%s, %d" %(str(self.content), self.index)

class Goal:
    def __init__(self):
        self.index = -1
        self.weight = 0
        self.max = float("-inf")
        self.min = float("inf")

h = Header()
rows = []

def convert_to_num(value):
    try:
        val = int(value)
    except ValueError:
        val = float(value)
    return val

def parse_header(index, value):
    global h
    h.name.append(value)
    if "?" in value:
        h.ignore.append(index)
    elif "%$" in value or "<" in value or ">" in value:
        h.num.append(index)
        if "<" in value or ">" in value:
            g = Goal()
            g.index = index
            if "<" in value:
               g.weight = -1
            else:
               g.weight = 1
            h.goal.append(g)
    else:
        h.sym.append(index)

def max_min(content):
    global h

    for i, goal in enumerate(h.goal):
        val = content[goal.index]
        goal.max = max(goal.max, val)
        goal.min = min(goal.min, val)
    return

def dominate(x, y):
    global h
    global rows

    sum1 = 0
    sum2 = 0
    e = 2.71828

    n = len(h.goals)

    for goal in header.goals:
        weight = goal.weight
        index = goal.index
        mx = goal.max
        mn = goal.min
        norm_x = (x[index] - mn) / (mx - mn)
        norm_y = (y[index] - mn) / (mx - mn)
        sum1 = sum1 - e**(weight * (norm_x - norm_y)/ n)
        sum2 = sum2 - e**(weight * (norm_y - norm_x)/ n)
    return sum1/n < sum2/n

def dom_rank(index, row):
    global rows
    rank = 0
    for i, val in enumerate(rows):
        if i != index:
            if dominate(row.content, val.content):
                rank += 1
    return rank

#data_to_be_traversed = reading_csv.Preprocessor().remove_extranous_attribute_and_type_caste_numeric_values('auto.csv')

#for r in data_to_be_traversed:
with open(sys.argv[1], "rb") as fp:
    # Header
    #for index, value in enumerate(str(r).rstrip().split(',')):
    for index, value in enumerate(fp.readline().rstrip().split(',')):
        parse_header(index, value)

    # Rows
    #for index, value in enumerate(str(data_to_be_traversed[1:-1])):
    for index, value in enumerate(fp.readlines()):
        row = Row()
        row.content = value.rstrip().split(',')
        row.index = index
        for col in h.num:
            row.content[col] = convert_to_num(row.content[col])

        max_min(row.content)
        rows.append(row)
    print h

    for index, row in enumerate(rows):
        row.rank = dom_rank(index, row)

