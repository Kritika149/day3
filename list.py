'''
list=ordered collection of items
eg: numbers=[1,2,3,4]
'''

list_of_numbers=[1,2,3,4,5]
list_of_names=["kritika","samaya","aaryama"]
list_of_even_numbers=[2,4,6]
list_of_odd_numbers=[1,3,5]

for i in list_of_even_numbers:
    print(f"{i}\n")
print(list_of_odd_numbers)
list_of_odd_numbers[2]=False
print (list_of_odd_numbers)



#add data to list
list_of_numbers.append(6)
list_of_numbers.insert(2,11)
print(list_of_numbers)
list_of_names.insert(2,11)
print(list_of_names)

fruits1=["apple","mange","banana"]
fruits2=["grapes","watermelon","guava"]
fruits1.pop(0)
print (fruits1)
deleted_items=fruits1.pop(0)


print(sorted(fruits2))   #creates duplicate
print(fruits2.count("grapes"))
fruits2.sort()    #changes the list
fruits2.reverse()
fruits3=fruits2.copy()
print(fruits2)
fruits2.clear()

print(fruits2)
print(fruits3)


#is vs equal

fruits5=["apple","mango", "banana"]
fruits6=["apple","mango", "banana"]

print(fruits5==fruits6) 
print(fruits5 is fruits6)
print(fruits5 is fruits5)




def give_me_list(num):
    my_list=[]
    for i in range(0,num+1):
        my_list.append(i)
    return my_list
mero_list=give_me_list(10)
print(mero_list)



user_number=int(input("enter a number"))
def cube_list(num):
    cube_list=[]
    for i in range(0,num+1):
    
        cube_list.append(i**3)
    return cube_list

mero_list_2=cube_list(user_number)  
print(mero_list_2) 



    











