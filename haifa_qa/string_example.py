
full_name = "Leo Messi"
name = "John Johnson"
# find the length of a string ~9
l = len(full_name)

length = len(full_name)
index_1 = full_name.index(" ")
index_2= name.index("oh")

#slicing examples
first_name= full_name[0:index_1]
last_name = full_name[index_1+1:length]
first_name_ver1 = full_name[:index_1]  # without prefix  - it will auto define as 0
last_name_ver1= full_name[index_1:]  # without suffix - it will define as the length of the string
s_counter = full_name.count("s")
name.count("John")
full_name  =full_name.replace("Leo", "Leonid")
slicing_single_number = full_name[0]





print ("test end")