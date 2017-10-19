# HW5

## Description:
Our contrast learner will examine each pair of nodes in the decision tree and report the delta and effect between each node in a pair

  * The delta is the difference in the branch path between each node
  * The effect is the mean difference in the performance score those nodes

Note that if the delta is:

  * positive then the contrast is a plan (something to do).
  * negative then the contrast is a monitor (something to watch for).

Note also that is statistically there is no difference between the population of instances in each node, then there is no point printing that contrast. For code to conduct those statistical tests, see same in num.

Test: Using auto.csv, print the plans and monitors separately. Note that for the leaves with best scores, there should be no plans generated. Similarly, for the leaves with worst scores, there should be monitors generated.


### Files:
1. Discretization.py  - Decision tree learner
2. Range.py - Unsupervised ranges creation
3. Superrange.py - Supervised ranges creation
4. Num.py - Code for numeric values
5. tree.py - Generates tree for auto.csv and finds Plan and Monitor among each pair of leaf nodes

 
 
### Execution Steps:

* The code runs in Python 2.7
* For executing the code, enter the folder containing all the codes and type following in the terminal:

```
> python tree.py
```
