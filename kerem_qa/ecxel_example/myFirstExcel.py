import csv

data = [{'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
        {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1}
    , {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3}
    , {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5}
    , {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8}
    , {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}]


field_names = ['name', 'branch', 'year', 'cgpa']


with open('university_records_v1.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
