#to reverse a given list using pop
list_of_names=["kritka","prashansa","sangita"]
def rev_a_list(given_lists):
    reversed_list=[]
    for item in given_lists:
        popped_item=given_lists.pop()
        reversed_list.append(popped_item)
    return reversed_list
abc=rev_a_list(list_of_names)    
print(abc)


#to reverse items in a given list
list_of_fruits=["apple","banana","watermelon"]
def reverse_item_list(given_list):
    reverse_items=[]
    for items in given_list:
        reverse_items.append(items[::-1])
    return reverse_items
ret_val=reverse_item_list(list_of_fruits)
print(ret_val)


#to filter odd and evenn and store the two lists within a list

num=int(input("enter a number"))
list_of_number=list(range(0,num+1))
def odd_even_filtered_list(odd_even):
    odd_list=[]
    even_list=[]
    for i in odd_even:
        if i%2==0:
            odd_list.append(i)
        else:
            even_list.append(i)
    return [odd_list,even_list]

returned_values=odd_even_filtered_list(list_of_number)
print(returned_values)

#to count no. of lists withing a list

def count_list(filtered_list):
    count_rate=0
    for elements in filtered_list:
        if type(elements)==list:
            count_rate +=1
    return count_rate

xyz=count_list(returned_values)
print(xyz)
    

