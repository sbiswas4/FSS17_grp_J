'''
Created on 09-Sep-2017

@author: advai
'''
from __future__ import division
import sys
the ={'ignore':'?'}

def create():
    return {'n':0,'mu':0,'m2':0,'sd':0,'hi':-sys.maxint,'lo':sys.maxint,'w':1}

def update(row_document_info,x):
        row_document_info['n'] = row_document_info['n'] +1
        if x < row_document_info['lo']:
            row_document_info['lo'] = x
        if  x > row_document_info['hi']:
            row_document_info['hi'] = x    
        delta = x - row_document_info['mu']
        row_document_info['mu'] = row_document_info['mu'] + delta/row_document_info['n']
        row_document_info['m2'] = row_document_info['m2'] + delta*(x- row_document_info['mu'])
        if row_document_info['n']>1:
            row_document_info['sd'] = (row_document_info['m2']/(row_document_info['n'] - 1))**0.5
        return row_document_info



def norm(goal_col_document,row_value):
    return (row_value-goal_col_document['lo'])/(goal_col_document['hi'] - goal_col_document['lo'] + 0.0000001)




