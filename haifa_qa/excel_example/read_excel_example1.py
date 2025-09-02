import csv

from haifa_qa.excel_example.globals_excel import FILE_NAME

names = []
with open(FILE_NAME, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row) # getting data as row
        print(row[0]) # getting data from spesific col.
        names.append(row[0])