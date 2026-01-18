from selectors import SelectSelector


def age_calculator(age):
    if age>20:
        print("age is greater than 18")
        age_new =age+5
    else :
        print("age is less than 18")
        age_new =age-5

    return age_new

    # staring the code

user_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "abc@abc.com",
    "age": 42


}

user_2 = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "john@abccom",
    "age": 16

}

age_1 = age_calculator(user_1["age"])
age_2 = age_calculator(user_2["age"])
print (f"{age_1} and  {age_2}")
# if user_1["age"] > 18:
#     print ("age is greater than 18")
# else:
#     print ("age is less than 18")
#
#
# if user_2["age"] > 18:
#     print ("age is greater than 18")
# else:
#     print ("age is less than 18")