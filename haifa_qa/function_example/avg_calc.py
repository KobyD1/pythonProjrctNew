from haifa_qa.function_example.utils import utils

utils_qa = utils()

avg_1 = utils_qa.get_avg(34,12)
avg_2 = utils_qa.get_avg(2,6)

if (avg_2>avg_1):
    print (f"avg2 is bigger VS avg1- avg1={avg_1} avg2={avg_2}")

else:
    print (f"avg1 is bigger VS avg2 - avg1={avg_1} avg2={avg_2}")


utils_qa.add_vat_to_price("26$")

