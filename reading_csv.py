'''
Created on 25-Aug-2017

@author: advait
'''
import sys
import pandas as pd
import csv
from pprint import pprint

class Preprocessor(object):
    
    def read_input_file_and_convert_to_list(self,file_to_be_preprocessed):
        # we must first overwrite the file to make sure the rows are aligned
        document_list=[]
        file_writing=open('aligned_file.csv','wb')
        with open(file_to_be_preprocessed) as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                document_list.append(row)
        return document_list       
    
    def align_rows(self,file_to_be_preprocessed):
        converted_document_to_list = Preprocessor().read_input_file_and_convert_to_list(file_to_be_preprocessed)
#     pprint(converted_document_to_list)
        print len(converted_document_to_list)
        size_of_list = len(converted_document_to_list)
        for i in range(size_of_list-1):
            if len(converted_document_to_list[i]) < len(converted_document_to_list[0]) and not converted_document_to_list[i][-1].strip() :
                converted_document_to_list[i].pop()
                converted_document_to_list[i].extend(converted_document_to_list[i+1])
                converted_document_to_list.pop(i+1)
                size_of_list-=1
        return converted_document_to_list
    
    def white_space_removal(self,file_to_be_preprocessed):
        '''type correction left , also type can be found from column ($ -> numeric value i.e. float in example)'''
        converted_document_to_list = Preprocessor().align_rows(file_to_be_preprocessed)
        stripped_document=[]
        for row_vector in converted_document_to_list[:]:
            stripped_document.append([cell.strip() for cell in row_vector])
        return stripped_document
        

if __name__ == '__main__':
    # read file as a command-line arguement
#     file_to_be_preprocessed = sys.argv[1]
    file_to_be_preprocessed = 'sample2'
    document_data_frame = pd.DataFrame(Preprocessor().white_space_removal(file_to_be_preprocessed)[1:],columns=Preprocessor().white_space_removal(file_to_be_preprocessed)[0])
    print document_data_frame
#     pprint(white_space_removal)    
#     print type(white_space_removal[0][3])