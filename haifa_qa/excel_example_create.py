
import csv
import os
import shutil
import time

data = [   {'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
           {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1},
           {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3},
           {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5},
           {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8},
           {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}
           ]

fieldnames = ['name', 'branch', 'year', 'cgpa']

# current_millis = int(time.time() * 1000)

with open('data/example333.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# os.makedirs('dest1')
# shutil.copy('data/example1.csv', 'dest1/file.csv')



