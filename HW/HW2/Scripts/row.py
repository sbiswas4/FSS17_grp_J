'''
Created on 09-Sep-2017

@author: advai
'''
from __future__ import division
import num as NUM
import sym as SYM 
import random
def create():
    return {'id':random.random(),"cells":[]}

def update(row_document_info,cells,t):
    row_document_info['cells'] = cells
    for i,head in enumerate(t['all']['cols']):
        if head['what'] == 'SYM':
            update_to_document = SYM.update(head, cells[head['pos']])
            update_to_document
        else:
            update_to_document = row_document_info=NUM.update(head, cells[head['pos']])
            update_to_document
    return row_document_info, t   

def dominate1(row,another_row,t,total_number_of_rows):
    e,n=2.71828,len(t['goals'])
    sum1,sum2=0,0
    for col in t['goals']:
        w=col['weight']
        x=NUM.norm(col, row[col['pos']])
        y=NUM.norm(col, another_row[col['pos']])
        sum1=sum1 - e**(w*(x-y)/n)
        sum2=sum2 - e**(w*(y-x)/n)
    return sum1/n < sum2/n   

def dominate(row,t,data_list,total_number_of_rows):
    tmp = 0
    for x,another_row in enumerate(data_list):
            if dominate1(row, another_row, t,total_number_of_rows):
                tmp+=1
    return tmp           
    