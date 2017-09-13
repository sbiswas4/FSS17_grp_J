## Problem Description
Read each line, kill whitepsace and anything after comment characters (#), break each line on comma, read rows into a list of lists (one list per row), converting strings to numbers where appropriate. Note that some column headers contain ?: all such columns should be ignored.

Your code should contain checks for bad lines (and bad lines should be skipped over); i.e. symbols where numbers should be and wrong number of cells (we will say that row1 has the “right” length).


## Files
* readcsv.py: python file to execute the work for this assignment

* POM3A.csv: given input csv table file (last few lines of POM3A csv have error rows which get handled and logged )

* ProcessedFile.csv: cleaned output file (CSV format)

* ProcessedFile.txt: cleaned output file (txt format). Its purpose is to check if data has been correctly typecasted to its column type while reading.

_ log_file.txt: maintains record of rows formatted. It also informs us about the time it took to read , process and write the csv file given

### Description of functions
The Preprocessor class has functions that preprocess the input file.
* read_input_file_and_convert_to_list function: simply reads the file and makes a list of list 
* align_rows function: handles unleft comma values.
* white_space_removal function: removes whitespaces
* remove_extranous_attribute_and_type_caste_numeric_values function: it will remove values of cell with header starting with ? . It will also type caste values with headers with $ in them as float(numeric). This will also delete rows with non numeric values where numeric values should have been
* detect_wrong_number_of_cell function: will detect and delete rows with wrong number of cells  


### Instructions to execute:
* Assuming that you have installed python 2.7
* reading_csv.py takes input file as a command line argument.
* Enter the following line in the command prompt to run:

```
> python <path>/reading_csv.py <path>/POM3A.csv
```
* The output can be found in the directory through which code has been executed


