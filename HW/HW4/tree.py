import numpy as np
import csv
import Range
import math
import Superrange
import collections
from anytree import Node,RenderTree
import Num
from copy import deepcopy

root = None

independent_var = ["displacement","horsepower","model"]

class Tree:
    level = 0

    def Node(self,parent,children):
        self.parent = {}
        self.children = {}

    def first_value(self,x):
        return (x[0])

    def second_value(self,x):
        return (x[1])

    def flatten(self,x):
        if isinstance(x, collections.Iterable):
            return [a for i in x for a in self.flatten(i)]
        else:
            return [x]

    def bin_var(self,bins):
        number_of_bins = len(bins)
        variance = 0
        if any(isinstance(i, list) for y in bins for i in y) == False:
            variance = self.calculate_variance_of_bin(bins)
            number_of_items = len(bins)
            return (variance/number_of_items)
        for k in range(number_of_bins):
            var = self.calculate_variance_of_bin(bins[k])
            variance += var
        flat_bin = self.flatten(bins)
        number_of_items_in_entire_bin = len(flat_bin) / 2
        return (variance/number_of_items_in_entire_bin)

    def return_splitted_list(self,sorted_lst_dom,breaks):
        start = 0
        indexes = []
        splitted_list = []
        sorted_lst_dom = sorted(sorted_lst_dom)
        dom_column = [element[0] for element in sorted_lst_dom]
        for index, value in enumerate(breaks):
            if value in dom_column:
                i = max(loc for loc, val in enumerate(dom_column) if val == value)
                indexes.append(i)
        if len(indexes) < 1:
            return sorted_lst_dom
        for k in indexes:
            end = k+1
            l = sorted_lst_dom[start:end]
            splitted_list.append(l)
            start =  end
            ii = indexes[-1:]
            if indexes.index(k) == (len(indexes)-1) and (len(sorted_lst_dom) - start >= 1):
                l = sorted_lst_dom[start:len(sorted_lst_dom)]
                splitted_list.append(l)

        return(splitted_list)



    def take_independent_dependent_columns(self,column_to_be_included):
        lst_dom = []
        with open("auto_dom.csv", "r") as inputFile:
            count = 0
            reader = csv.reader(inputFile, delimiter=",")
            included_columns = column_to_be_included
            for row in reader:
                count += 1
                if count == 1:
                    continue
                content = list(float(row[i]) for i in included_columns)
                lst_dom.append(content)
        return lst_dom


    def calculate_variance_of_bin(self,bin):
        num_of_items = len(bin)
        dom_values = [element[1] for element in bin]
        variance_in_dom = np.var(dom_values)
        #print("num of items",num_of_items)
        return(num_of_items*variance_in_dom)

    def read_data(self):
        column_to_be_included = [1,2,5,8]
        lst_dom = []
        with open("auto_dom.csv", "r") as inputFile:
            count = 0
            reader = csv.reader(inputFile, delimiter=",")
            included_columns = column_to_be_included
            for row in reader:
                count += 1
                if count == 1:
                    continue
                content = list(float(row[i]) for i in included_columns)
                lst_dom.append(content)
        return(lst_dom)

    def main(self):
        independent_col = [1,2,5]
        dep_col = 8
        variance_of_bins = []
        all_bins = []
        for i in independent_col:
            content = self.take_independent_dependent_columns([i,8])
            sorted_content = sorted(content)
            r = Range.main(sorted_content,self.first_value)
            breaks = Superrange.main(r,self.second_value)
            len_breaks =len(breaks)
            bins = self.return_splitted_list(content,breaks)
            all_bins.append(bins)

        for bin in all_bins:
            var = self.bin_var(bin)
            variance_of_bins.append(var)
        final_tree = self.create_tree(all_bins,variance_of_bins)

    def call_Num_for_nested_list(self,lst,key):
        num_output = []
        if any(isinstance(i, list) for y in lst for i in y) == False:
            num_output = Num.updates(lst,self.second_value,None)
            num_output.independent_column = key
        else:

            for k in range(len(lst)):
                num_op = Num.updates(lst[k],self.second_value,None)
                num_op.independent_column = key
                num_output.append(deepcopy(num_op))
        return num_output

    def return_summarized_output(self,dict,independent_columns):
        sd = float('Inf')
        return_list = []
        for key in independent_columns:
            output = self.call_Num_for_nested_list(dict[key],key)
            return_list.append(output)

        return return_list

    def return_bin_with_least_variance(self,list_of_bins):
        min_var = float('Inf')
        least_sd_bin = []
        index_of_least_bin = 0
        for i in range(len(list_of_bins)):
            sd_var = 0
            len_of_bin = 0
            for j in range(len(list_of_bins[i])):
                sd_var += list_of_bins[i][j].n * list_of_bins[i][j].variance
                len_of_bin += (len(self.flatten(list_of_bins[i][j].elements))/2)

            sd_var = sd_var/len_of_bin
            if sd_var < min_var:
                min_var = sd_var
                least_sd_bin = list_of_bins[i]
                index_of_least_bin = i
        return(index_of_least_bin,least_sd_bin)

    def create_tree(self,all_bins,variance_of_bins):
        bin_dict = {}
        independent_columns = ["displacement","horsepower","model"]
        position_of_bin_minvar = 0
        bins_to_consider = all_bins
        for i in range(len(bins_to_consider)):
            bin_dict.update({independent_columns[i]:bins_to_consider[i]})
        op = self.return_summarized_output(bin_dict,independent_columns)
        least_bin = self.return_bin_with_least_variance(op)
        level = 0
        summary = self.return_summarized_output(bin_dict, independent_var)
        parent_columns = bin_dict.keys()
        sum_all = []
        for s in range(len(summary)):
            sum = {key: summary[s][0].__dict__[key] for key in ["independent_column", "n", "variance"]}
            sum['x'] = sum['independent_column']
            sum['sd'] = math.sqrt(sum['variance'])
            sum['sd'] = float("{:.2f}".format(sum['sd']))
            sum = {key: sum[key] for key in ["x", "n", "sd"]}
            sum_all.append(sum)
        root = Node(sum_all)

        count_dict = {"displacement":0,"horsepower":0,"model":0}
        n_parent = 0
        tree = self.build_tree(bin_dict,None,independent_columns,level,root,count_dict,n_parent)
        for pre, fill, node in RenderTree(tree):
            print("%s%s" % (pre, node.name))

    def get_bins(self, bin_dictionary, column_name):
        return_bins = {}
        master_list = []
        key = bin_dictionary.keys()
        lst_dom = self.read_data()
        index_parent = independent_var.index(key[0])
        indexes_of_columns = []
        for c in column_name:
            index_col = independent_var.index(c)
            indexes_of_columns.append(index_col)
        list_to_look_up = bin_dictionary.values()[0]

        for index in indexes_of_columns:
            list_to_return = []
            for lst in list_to_look_up:
                for lst_d in lst_dom:
                    if lst[0] in lst_d and lst[1] in lst_d:
                        if lst[0] == lst_d[index_parent] and lst[1] == lst_d[3]:
                            list_to_return.append([lst_d[index],lst_d[3]])
            master_list.append(deepcopy(list_to_return))
        sorted_master_list = []
        for k in range(len(master_list)):
            sorted_l = sorted(master_list[k])
            r = Range.main(sorted_l,self.first_value)
            breaks = Superrange.main(r,self.second_value)
            len_breaks = len(breaks)
            bins = self.return_splitted_list(sorted_l, breaks)
            bin_dict = {column_name[k]:bins}
            return_bins.update(bin_dict)
            sorted_master_list.append(deepcopy(sorted_l))

        return(return_bins)

    def find_children(self,bin_dictionary,independent_columns):
        if len(independent_columns) == 3:
            op = self.return_summarized_output(bin_dictionary,independent_columns)
            i,least_bin = self.return_bin_with_least_variance(op)
            return (i, least_bin)
        else:
            bin_children_dict = self.get_bins(bin_dictionary,independent_columns)
            op = self.return_summarized_output(bin_children_dict, independent_columns)
            i, least_bin = self.return_bin_with_least_variance(op)

            return(i,least_bin)

    def build_tree(self,bin_dictionary,parent,independent_var,level,root,count_dict,n_parent):

        index,children = self.find_children(bin_dictionary,independent_var)

        level +=1
        for k in range(len(children)):
            ind_var = ["displacement","horsepower","model"]
            child = { key: children[k].__dict__[key] for key in ["independent_column","n","variance"] }
            if n_parent == child['n']:
                continue

            child['sd'] = math.sqrt(child['variance'])
            child['sd'] =  float("{:.2f}".format(child['sd']))
            count_dict[child['independent_column']] +=1
            child['x'] = child['independent_column'] + str(count_dict[child['independent_column']])
            child = {key: child[key] for key in ['x', 'sd', 'n']}

            del ind_var[index]
            bin_dict_for_next_level = {independent_var[index]:children[k].elements}
            node_name = Node(child,parent = root)
            if level < 4:
                self.build_tree(bin_dict_for_next_level, independent_var[index], ind_var, level,node_name,count_dict,child['n'])
        return root



t = Tree()
t.main()
