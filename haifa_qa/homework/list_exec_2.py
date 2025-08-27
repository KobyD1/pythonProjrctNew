numbers = [23,8,11,3,4,-5,6,-12]
numbers_with_zero = [2,4,3,0,12,67]

# 1. print all numbers that dived by 2
# 2.make summery of all positive numbers and negative numbers
# 3. calculate the summery of all numbers until we get 0
summery_positive = 0
summery_negative = 0

for number in numbers:
    if (number%2==0):
        print (number)

    if (number>0):
        summery_positive = summery_positive+number

    else:
        summery_negative = summery_negative+number

print(f"Summery negative{summery_negative}")
print(f"Summery pos{summery_positive}")

