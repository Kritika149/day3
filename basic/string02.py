
'''
first_name,second_name= input("please enter full name (space separated):").split(" ")
print ("your full name is ==>" + first_name+" "+ second_name)
first_name,second_name= input("please enter full name (comma separated):").split(",")
print ("your full name is ==>" + first_name+" "+ second_name)

#type function"
name_type=type(first_name)
print (name_type)
'''
'''
first_no,second_no,thirdt_no= (input("enter 3 numbers ( comma separated): ".split(","))
sum= int(first_no)+int(second_no)+int(thirdt_no)
average=sum/3
print(" the average is ==", average)
'''

#string indexing
'''
name="Language"
print(name)
print(name[3])
print(name[-1])
print(name[1:3]) #last one is not included (exclusive)
print(name[1:7:2]) #last t"2" indicates steps to skip
print(len(name))
print(name[::-1]) #to reverse
print (name[-1::-1]) #to reverse
print(name[-1::5])
'''

#string method
example="kritika"
print(example.lower())
print(example.upper())
print(example.title())

print(example.count("i")) #count is case sensitive

fullname,char= input("please enter full name and character (space separated):").split(" ")
# full_name= first_name+ second_name
char_count = fullname.lower().count(char)


print("your full name is {} and '{}' char count is {}".format(fullname,char ,char_count))
print(f"your fullname is {fullname} and '{char}' amd char count is {char_count}")



fullname,char= input("please enter full name and character (comma separated):").split(",")
space=fullname.strip()
char_count=fullname.lower().count(char.strip())
print("My name is"+ fullname + "and" , char_count)









