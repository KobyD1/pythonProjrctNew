price  = '29.99$'
price = price.replace("$","")
indx = price.index(".")
price=price[:indx]
print (price)