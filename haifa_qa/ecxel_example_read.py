import csv
names = []
with open('data/example.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row) # getting data as row
        print(row[0]) # getting data from spesific col.
        names.append(row[0])

print ("test end")





