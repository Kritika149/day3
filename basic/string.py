''''


print(r"This is \\ double backslash")
print("This is \\\\double backslash")
print(2+3)
print(9-3)
print(9/3)
print(9//3)
print(9*3)
print(9**3)
print(9%2)
print("\U0001F602")
print(3*3.12546)
print(round(3*3.12546,3))
#string concatenation
print("Aryama"+"Rushav")
print("Aryama"+" "+"Rushav") #to give space using +
print("Aryama"+str(10))
print(10+int("10"))
#variable in python
a=10
print(a)
print("the first value of a is: -->" , a)
a= "apple"  #a is dynamic
print("the first value of a is: -->" , a)
#Variable in python


numeric_value ==> snake_case_writing (reccommended for python)
numericvalue ==> cameCasewriting






numeric_value=10
fruit_name="apple"
print (numeric_value)
print (fruit_name)

#user input
user_provided_fruit =input("please give your provide food")
print("the first value of a is ==> ",user_provided_fruit)

user_provided_firstname=input("first name")
user_provided_second_name=input("second name")
print("your full name is " ,user_provided_firstname + " "+ user_provided_second_name)

#numeric calculations
print(18+12)  #addition
print(18-12)  #substraction 
print(18*2)   #multiplication 
print(3**3)   #power 
print(3/2)    #int division 
print(3//2)   #division (no int only quotient)
print(3%2)    #modulo 
print(round(22/7,2)) #rounding off
print((9+1)*2+10)   #bodmas 


#string concatenation

a="kriitka"
b="deo"
print("My name is ", a ,b)
my_name=a+" "+b    #to give space
print("I am", my_name)

# to convert integer into string
print ("My usernmae is github is","kritika"+ str(149))

#to convert string into integer
print("my age is ==>", 10+int("8"))

# to print emoji
print("\U0001F436	") # use webbsite unicode and use 000 in place of +

#variable and input function

user_input_day=input("todays day")
user_input_month=input("todays date")
user_input_year=input("todays year")
user_input_date=input("todays date")
date_today= user_input_date +"/"+user_input_month +"/"+user_input_year + ","+ user_input_day
print("today is ==> ", date_today)



'''




#Day4
'''
#type function (to find the type of a variable)
name=input("whats your name")
print("Myname is ==>"+name)
type_name=type(name)
print (type_name)

#to print average of 3 numbers
a,b,c=input("enter 3 numbers separated by comma:").split(",")
sum=int(a)+int(b)+int(c)
average=sum/3
print("the average is ",average)
print(type(sum))
print(type(average))
'''
#string indexing

'''


word='What is your name?'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])
print(word[7])
print(word[-1])
print(word[8:12])
print(word[-1::-1])
print(word[3:16:2]) #to print from 4th to 15th at steps of 2
print(len(word))   #to print no. of characters

'''
'''
#to lowercase and usppercase
name1="HEHE"
name2="whatt"
print(name1.lower())
print(name2.upper())

#to capitalize only the first letters of every word
sentence="today is thursday"
print(sentence.title())
'''
#to count only a particular character
a="kritika"
print(a.count("i"))

