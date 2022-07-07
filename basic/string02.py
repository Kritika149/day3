
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
 '''
space_problem="  aryama  "
# full_name, character =input("enter your full name and character you want to count (comma separated)").split(",")
# charcount= full_name.lower().count(character.strip())
# print(f"your name is {full_name} the character to count is {character} the character name is {charcount}")


# replace
solved_problem = space_problem.replace(" ","")
print(f"the solve of space problem is : {space_problem}")

replace_example = "Kritika is a beautiful and she is out standing."
print(replace_example.replace("is","was",1))
is_position1 = replace_example.find("is")
print(replace_example.find("is",is_position1+1))

#center() method
example2="python"
print(example2.center(2+6+2,"*"))
full_name=input("enter full name")
a=len(full_name)
print(full_name.center(5+a+5,"*"))

#string are immutable and assignment operator
example3="any"
example3[1]="N"
replaced_example= example3.replace("n","N")
print(replaced_example)
example3= example3+ "body"
example3 += "body"
print(example3)













