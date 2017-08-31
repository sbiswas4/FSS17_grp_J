import sys
from pprint import pprint
import time
import re


class Preprocessor(object):
    def read_input_file_and_convert_to_list(self, file_to_be_preprocessed):
        # we must first overwrite the file to make sure the rows are aligned
        document_list = []
        file_writing = open('aligned_file.csv', 'wb')
        with open(file_to_be_preprocessed) as input_file:
            content = input_file.read().splitlines()
            for sentence in content:
                document_list.append(sentence.split(","))
        return document_list

    def align_rows(self, file_to_be_preprocessed):
        converted_document_to_list = Preprocessor().read_input_file_and_convert_to_list(file_to_be_preprocessed)
        size_of_list = len(converted_document_to_list)
        for i in range(size_of_list - 1):
            if len(converted_document_to_list[i]) < len(converted_document_to_list[0]) and not \
            converted_document_to_list[i][-1].strip():
                converted_document_to_list[i].pop()
                converted_document_to_list[i].extend(converted_document_to_list[i + 1])
                log = "Removing unaligned rows : " + str(converted_document_to_list[i+1])
                logFile.append(log)
                converted_document_to_list.pop(i + 1)
                size_of_list -= 1
        return converted_document_to_list

    def white_space_removal(self, file_to_be_preprocessed):
        converted_document_to_list = Preprocessor().align_rows(file_to_be_preprocessed)
        stripped_document = []
        for row_vector in converted_document_to_list[:]:
            stripped_document.append([cell.strip() for cell in row_vector])
        return stripped_document

    def remove_comments(self, file_to_be_preprocessed):
        data_list_of_list = Preprocessor().detect_wrong_number_of_cell(file_to_be_preprocessed)
        for j in range(len(data_list_of_list)):
            for i in range(len(data_list_of_list[0])):
                data_list_of_list[j][i] = re.sub(r'\t*\s*#.*', '', data_list_of_list[j][i])
        return data_list_of_list

    def remove_extranous_attribute_and_type_caste_numeric_values(self, file_to_be_preprocessed):
        data_list_of_list = Preprocessor().remove_comments(file_to_be_preprocessed)
        index_of_disqualified_attribute = []
        numeric_value = []
        for header in data_list_of_list[0]:
            if header.find('?') == 0:
                index_of_disqualified_attribute.append(data_list_of_list[0].index(header))
            elif header.find('$') != -1:
                numeric_value.append(data_list_of_list[0].index(header))
        number_of_index_shifted = 0
        for i in range(len(index_of_disqualified_attribute)):
            for row_vector in data_list_of_list:
                row_vector.pop(index_of_disqualified_attribute[i] - number_of_index_shifted)
            number_of_index_shifted += 1

        number_of_rows = len(data_list_of_list)
        i = 1
        while i < number_of_rows:
            try:
                for j in numeric_value:
                    data_list_of_list[i][j] = float(data_list_of_list[i][j])
                i += 1
            except ValueError:
                log = "Symbols where numbers should be in row " + str(i+row_shifted) + ": Found " + data_list_of_list[i][j] + " in cell " + str(j+1) #+ str(data_list_of_list[i])
                logFile.append(log)
                data_list_of_list.pop(i)
                number_of_rows -= 1
                pass
        return data_list_of_list

    def detect_wrong_number_of_cell(self, file_to_be_preprocessed):
        data_list_of_list = Preprocessor().white_space_removal(file_to_be_preprocessed)
        number_of_rows = len(data_list_of_list)
        global row_shifted
        row_shifted = 1
        i = 1
        while i < number_of_rows:
            if len(data_list_of_list[i]) < len(data_list_of_list[0]):
                log = "Number of cells is less than number of attributes in row " + str(i+row_shifted)  + ": " + str(data_list_of_list[i])
                logFile.append(log)
                data_list_of_list.pop(i)
                number_of_rows -= 1
                row_shifted +=1
            elif len(data_list_of_list[i]) > len(data_list_of_list[0]):
                log = "Number of cells is more than number of attributes in row " + str(i+row_shifted)  + ": " + str(data_list_of_list[i])
                logFile.append(log)
                data_list_of_list.pop(i)
                number_of_rows -= 1
                row_shifted += 1
            else:
                i += 1
        return data_list_of_list


if __name__ == '__main__':
    # read file as data_list_of_list command-line arguement
    #     file_to_be_preprocessed = sys.argv[1]
    start_time = time.time()
    file_to_be_preprocessed = 'POM3A.csv'
    logFile=[]
    data_list_of_list = Preprocessor().remove_extranous_attribute_and_type_caste_numeric_values(file_to_be_preprocessed)
    with open("ProcessedFile.csv", "w") as output:
        for row in data_list_of_list:
            for value in row:
                output.write(str(value)+',')
            output.write("\n")
    with open("ProcessedFile.txt", "w") as output:
        for row in data_list_of_list:
            output.write(str(row))
            output.write("\n\n")
    log_file = open('log_file.txt', 'w')
    for element in logFile:
        log_file.writelines((element))
        log_file.write("\n")
    log_file.write("The program took {} seconds to read and process {} file".format(time.time() - start_time,file_to_be_preprocessed))
