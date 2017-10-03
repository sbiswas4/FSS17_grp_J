# HW4 

## Description:
To build a regression tree learner:

Apply supervised Discretization at each level of the tree, break the data on the ranges and find the column whose breaks most reduces the variability of the target variable (we will use dom).

For each break, apply the regression tree learner recursively. Recursion stops when the breaks do not improve the supervised target score, when there are tooFew examples to break, or when the tree depth is too much.

Write a list printer that recurses down the tree and prints details about each node, indented by its level in tree.


### Files:
1. Discretization.py  - Decision tree learner
2. Range.py - Unsupervised ranges creation
3. Superrange.py - Supervised ranges creation
4. Num.py - Code for numeric values
5. tree.py - Generates tree for auto.csv

 
 
### Execution Steps:

* The code runs in Python 2.7
* For executing the code, enter the folder containing all the codes and type following in the terminal:

```
> python tree.py
```
