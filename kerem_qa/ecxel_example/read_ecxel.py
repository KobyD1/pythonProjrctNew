import csv

with open("university_records_v1.csv", mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # Method 1a: Print all rows as lists
    print("--- Reading All Rows ---")
    for row in csv_reader:
        print(row)
        print (row[1])