'''
Created on 10-Sep-2017

@author: advait
'''
import sys
import row as ROW
import num as NUM
import sym as SYM
import reading_csv
import pprint

# Function to create a new table
def create():
    rows=[]
    specs=[]
    goals=[]
    less=[]
    more=[]
    name=[]
    all = {'nums':[],'syms':[],'cols':[]}
    x = {'nums':[],'syms':[],'cols':[]}#all independent cols go in x
    y = {'nums':[],'syms':[],'cols':[]}#all dependent cols go in x
    return {"rows":rows,'specs':specs,'goals':goals,'less':less,'more':more,'name':name,'all':all,'x':x,'y':y}

# Categories in table where respective numeric and symbolic columns must be updated
def categories(i,txt):
  local_spec =  [
    {'when':"$", 'what': 'NUM', 'weight':1, 'where':[i['all']['cols'], i['x']['cols'], i['all']['nums'],i['x']['nums']]},
    {'when':"<",  'what': 'NUM', 'weight':-1, 'where':[i['all']['cols'], i['y']['cols'], i['all']['nums'], i['goals'], i['less'], i['y']['nums']]},
    {'when': ">",  'what': 'NUM', 'weight': 1, 'where': [i['all']['cols'], i['y']['cols'], i['all']['nums'], i['goals'], i['more'], i['y']['nums']]},
    {'when':"!",  'what': 'SYM', 'weight': 1, 'where': [i['all']['cols'], i['y']['syms'], i['y']['cols'],   i['all']['syms']]},
    {'when': "",   'what': 'SYM', 'weight': 1, 'where': [i['all']['cols'], i['x']['cols'],             i['all']['syms'],      i['x']['syms']]}                 
    ]
  for _,want in enumerate(local_spec) :
          if str(txt).find(want['when']) != -1:
              return want['what'], want['weight'], want['where'] 

# to make attributes of each header in the table
def header(i,cells):
    i['specs'] = cells
    for col,cell in enumerate(cells):
        what,weight,wheres = categories(i, cell)
        wh = NUM if (what == 'NUM') else SYM
        one = wh.create()
        one['pos'] = col #added new key pos
        one['txt'] = cell
        one['what'] = what
        one['weight'] = weight
#         i['name'][one['txt']] = one
        for where in wheres:
            where.append(one) 
    return i

# Table value gets updated row by row, NOTE: am not storing the row value as per lua code so table doesn't have an empty row
def data(dummy_table,cells):
    new,table = ROW.update(ROW.create(),cells,dummy_table)
#     table['rows'].append(new)
#     if old:
#         new['id'] = old['id']
    return table  
  
#Not using this function         
def update(row_document_info,cells):
    if len(row_document_info['specs']) == 0 : 
        return header(row_document_info,cells) 
    else:
        return data(row_document_info,cells)
      
''' ENTRY POINT'''
file_to_be_processed = sys.argv[1]   
data_to_be_traversed = reading_csv.Preprocessor().remove_extranous_attribute_and_type_caste_numeric_values(file_to_be_processed)

# Reading rows and updating
for row_index in range(len(data_to_be_traversed)):
     if row_index == 0:   
        dummy= create()
        dummy =(header(dummy,data_to_be_traversed[0]))
     else:
         table =data(dummy,data_to_be_traversed[row_index])
# pprint.pprint(table)                   
with open('TableStructure.txt', 'w') as out:
    pprint.pprint(table, stream=out)

print "Dominate Score"

dominate_dictionary={}
for i,row in enumerate(data_to_be_traversed):
    if i!=len(data_to_be_traversed) and i!=0:    
        dominate_dictionary[i]=ROW.dominate(row, dummy,data_to_be_traversed[1:],len(data_to_be_traversed)-1)

from operator import itemgetter, indexOf
dom =sorted(dominate_dictionary.items(), key=itemgetter(1))
max_dominate_indexer = [i[0] for i in dom[-5:]]
min_dominate_indexer = [i[0] for i in dom[:5]]
max_dominate_indexer = reversed(max_dominate_indexer)
min_dominate_indexer = reversed(min_dominate_indexer)
with open('DominationScores.txt','w') as f:
    print 'file writing'
    f.write(str(data_to_be_traversed[0]))
    f.write('\n Most Dominant\n')
    for i in max_dominate_indexer:
        f.write(str(data_to_be_traversed[i]))
        f.write('\n')
    f.write('\nLeast Dominant \n')
    for i in min_dominate_indexer:
        f.write(str(data_to_be_traversed[i])) 
        f.write('\n')   

print "Program Finish"    