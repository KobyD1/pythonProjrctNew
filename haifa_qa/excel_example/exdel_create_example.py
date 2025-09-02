import csv
import os

from haifa_qa.excel_example.globals_excel import FILE_NAME

headers = ['firstName','lastName','Age','Grade']

data = [
    {'firstName':'Johnson','lastName':'Johnson','Age':22,'Grade':90},
{'firstName':'Johnson1','lastName':'Johnson1','Age':33,'Grade':66},
{'firstName':'Shimrit','lastName':'Shimrit','Age':44,'Grade':33}

]

os.makedirs('../results', exist_ok=True)

with open(FILE_NAME, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)