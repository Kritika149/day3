

first_name,second_name= input("please enter full name (space separated):").split(" ")
print ("your full name is ==>" + first_name+" "+ second_name)
first_name,second_name= input("please enter full name (comma separated):").split(",")
print ("your full name is ==>" + first_name+" "+ second_name)

#type function
name_type=type(first_name)
print (name_type)

