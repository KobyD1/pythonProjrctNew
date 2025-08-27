
numbers_with_zero = [2,4,3,0,12,67]
numbers_with_zero.insert(1,23)
numbers_with_zero.append(444444)
summery =0
for number in numbers_with_zero:
    summery += number
    if (number ==0):
        break

print (summery)