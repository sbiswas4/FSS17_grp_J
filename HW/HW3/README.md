# Problem Statement


## Set up

The code is written in Python 2.7

## Brief Description of individual code files

### List_Discretization.py.py

* This is the master file which needs to be run. It calls functions from other files when needed. It calls reading_csv.py (Homework 1) and prepares csv file for Homework 2. 
* It replicates the functionality of tbl.lua with the same function names. It creates the table structure and updates it by calling header and data functionality when necessary when a new row is added
* It calls the dominate function and assigns dom score to each row and prints top 5 rows with highest dom scores and bottom 5 with the lowest dom score.

### Range.py

* Equivalent of sym.lua, it maintains and updates the knowledge of symbol counts

### Random.py

### Sample.py


### Num.py

* Equivalent to num.lua, it contains the update function for numeric column which maintains and updates the knowledge of mean and standard deviation


## Execution

* The python scripts are in scripts folder. Download the folder and enter the path in the command line as follows:

```
sudo python <path>List_Discretization.py
```

