

cities = ["Rome", "London","Milano"]
numbers = [2,4,6,3,26,6,12,1105555]

l = len(numbers)  # to find the length of the list
index_1 =numbers.index(6) # getting the index of the first 6 in the list
# adding object to list
numbers.append(34)
numbers.insert(2,15 )
if 2 in numbers:  # to check if list contains spesific value
    numbers.remove(2)

counter = numbers.count(6)
# reminder the count staert from 0
object_in_place_5= numbers[5]

for number in numbers:
    print (number)
    if (number>5):
        print (f"more than 5 number found the value is {number}")
