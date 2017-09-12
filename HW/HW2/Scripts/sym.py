'''
Created on 10-Sep-2017

@author: advai
'''
import csv
from collections import defaultdict


def create():
    return {'n':0, 'nk':0,'counts':{}, 'most':0,'mode':None,'_ent':None}
    


def Symbol_Count(data):#data is column
    frequency_table = create()
    for key in data:
        if key in frequency_table:
            frequency_table[key] += 1
        else:
            frequency_table[key] = 1
    return frequency_table

# def update(row_document_info,x):
#   if x != '?' :
#     row_document_info['_ent'] = None 
#     row_document_info['n'] = row_document_info['n'] + 1
#     if not row_document_info['counts'][x]:
#       row_document_info['nk'] = row_document_info['nk'] + 1
#       row_document_info['counts'][x] = 0 
#     seen = row_document_info['counts'][x] + 1
#     row_document_info['counts'][x] = seen 
#     if seen > row_document_info['most']:
#       row_document_info['most'], row_document_info['mode'] = seen,x 


def update(head,row_of_column_number): # i is head and x is column number
    keys = head['counts'].keys()
    if row_of_column_number in keys:
        head['counts'][row_of_column_number] +=1
    else:
        head['counts'].update({row_of_column_number:1})