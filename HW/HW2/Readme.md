# Problem Statement

Reading table: Find and print the top and bottom ten rows of auto.csv, as sorted by their dom score. with the top 5 and the bottom 5 domination scores.

## Set up

The code is written in Python 2.7

## Brief Description of individual code files

### tbl.py

* This is the master file which needs to be run. It calls functions from other files when needed. It calls reading_csv.py (Homework 1) and prepares csv file for Homework 2. 
* It replicates the functionality of tbl.lua with the same function names. It creates the table structure and updates it by calling header and data functionality when necessary when a new row is added
* It calls the dominate function and assigns dom score to each row and prints top 5 rows with highest dom scores and bottom 5 with the lowest dom score.

### sym.py

* Equivalent of sym.lua, it maintains and updates the knowledge of symbol counts

### row.py

* Synonymous to row.lua, it checks the type of the row, NUM/SYM and calls corresponding update function
* It also contains definition of dominate and dominate1 functions

### num.py

* Equivalent to num.lua, it contains the update function for numeric column which maintains and updates the knowledge of mean and standard deviation


## Execution

* The python scripts are in scripts folder and the input data auto.csv is in data folder. Download both the folders and enter their respective paths in the command line as follows:

```
python <path>/Scripts/tbl.py <path>/Data/auto.csv
```
