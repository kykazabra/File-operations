import csv
import pickle
import copy

def load_table_csv(file_name=''):
    if file_name == '':
        file_name = input('Введите имя файла, из которого вы хотите скопировать таблицу: ')
    rows = []
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            rows.append(row)
    rows[0][0] = rows[0][0].replace('п»ї', '')
    return rows

def save_table_csv(table, new_file_name=''):
    if new_file_name == '':
        new_file_name = input('Введите имя файла, в который вы хотите сохранить таблицу: ')
    with open(new_file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(table)
    return True

def load_table_pickle(file_name=''):
    if file_name == '':
        file_name = input('Введите имя файла, из которого вы хотите скопировать объект: ')
    with open(file_name, 'rb') as file:
        object = pickle.load(file)
    return object

def save_table_pickle(object, new_file_name=''):
    if new_file_name == '':
        new_file_name = input('Введите имя файла, в который вы хотите сохранить объект: ')
    with open(new_file_name, 'wb') as file:
        pickle.dump(object, file)
    return True

def filler(tablex):
    table = copy.deepcopy(tablex)
    max_len = 0
    for row in table:
        for yach in row:
            if len(yach) > max_len:
                max_len = len(yach)
    for i in range(len(table)):
        for j in range(len(table[i])):
            pered = 0
            szad = 0
            if len(table[i][j]) < max_len:
                diff = max_len - len(table[i][j])
                pered = diff//2
                szad = diff - pered
            table[i][j] = ' ' * pered + table[i][j] + ' ' * szad + ' '
    new_table = []
    for row in table:
        new_row = ''
        for obj in row:
            new_row += obj
        new_table.append(new_row)
    return new_table

def save_table_txt(table, new_file_name=''):
    new_table = filler(table)
    if new_file_name == '':
        new_file_name = input('Введите имя файла, в который вы хотите сохранить таблицу: ')
    with open(new_file_name, 'w') as file:
        for row in new_table:
            file.write(row + '\n')
    return True

def get_rows_by_number(table, start, stop = ''):
    if stop == '':
        stop = start
    return table[start-1:stop]

def get_rows_by_index(table, *values):
    new_table = []
    for row in table:
        if row[0] in values:
            new_table.append(row)
    return new_table

def get_column_types(table, by_number = True):
    types = {}
    for i in range(len(table[0])):
        if by_number:
            types[i+1] = type(table[1][i])
        else:
            types[table[0][i]] = type(table[1][i])
    return types

def get_values(table, column = 0):
    new_column = []
    if type(column) == str:
        column = table[0].index(column)+1
    for row in table:
        new_column.append(row[column-1])
    return new_column

def get_value(table, column = 0):
    if type(column) == str:
        column = table[0].index(column)+1
    return table[1][column-1]

def set_values(tablex, values, column = 0):
    table = copy.deepcopy(tablex)
    if type(column) == str:
        column = table[0].index(column)+1
    for i in range(1, len(table)):
        for j in range(len(table[i])):
            if j == column-1:
                table[i][j] = values[i-1]
    return table

def set_value(tablex, value, column = 0):
    table = copy.deepcopy(tablex)
    if type(column) == str:
        column = table[0].index(column)+1
    table[1][column-1] = value
    return table

def print_table(table):
    new_table = filler(table)
    for row in new_table:
        print(row)
    return True

def merge_tables(table1x, table2x, by_number = True):
    table1 = copy.deepcopy(table1x)
    table2 = copy.deepcopy(table2x)
    merged_table = []
    if by_number:
        for i in range(len(table1)):
            merged_row = []
            for j in range(len(table1[i])):
                merged_row.append(table1[i][j] + ' ' + table2[i][j])
            merged_table.append(merged_row)
    else:
        merged_row = []
        for k in range(len(table1[0])):
            merged_row.append(table1[0][k] + ' ' + table2[0][k])
        merged_table.append(merged_row)
        for i in range(1, len(table1)):
            for j in range(1, len(table2)):
                merged_row = []
                if table1[i][0] == table2[j][0]:
                    for k in range(len(table1[i])):
                        merged_row.append(table1[i][k] + ' ' + table2[j][k])
            merged_table.append(merged_row)
    return merged_table