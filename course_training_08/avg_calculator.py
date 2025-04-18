# grade_1 = 80
# grade_2 = 85
# grade_3 = 70
# sum = grade_1 + grade_2 + grade_3
# avg = sum /3
# print (avg)

grades = [80,45,39,78,90,95,95,100]
summery = 0

for grade in grades:
    print (grade)
    summery = summery + grade
    print (summery)

len_by_list = len(grades)
avg_by_list = summery/len_by_list
print (avg_by_list)
