# block to sample
try :
    a = 10
    b = 5
    num1 = 20
    num2 = a -b
    summery = num1/num2

    # what I looking for

except ZeroDivisionError:
    print ("Division by zero event found ")
    num2 =1
    summery = num1/num2
# will be done anyway
finally:
    summery = summery +5





print (summery)

