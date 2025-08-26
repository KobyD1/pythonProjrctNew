city =  "New-York"
counter =city.count("-")

print (f"the value is {counter}")

sentence = "My cat has 4 legs"

index_1 = sentence.index("has")+len("has")+1
index_2 = sentence.index("leg")
num = sentence[index_1:index_2]
print (num)
# 1.find in the name cat is in the sentence
# 2. print the substring '4 legs'
cat_counter= sentence.count("cat")
index =sentence.index("4")
l = len(sentence)
result = sentence[index:l]
print (result)


