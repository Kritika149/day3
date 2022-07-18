sets_any={"sunday","monday","tuesday"}
any_list=1,2,3,4,5,5,6,7,8,5,4,9
set_convert=set(any_list)
print(set_convert)
list_convert=list(set_convert)
print(list_convert)

# Distinguish set and dictionary while creating empty set

a = {}
print(type(a))
a = set()
print(type(a))

my_set={1,3}
# add an element
my_set.add(2)
print(my_set)

# add multiple elements
my_set.update([2,3,4,5,6])
print(my_set)

# add list and set
my_set.update([7,8,9],{10,11})
print(my_set)

# discard an element
my_set.discard(4)
my_set.discard(12)  #you can use smth not present in set without any erroe but in"remove an error occrs
print(my_set)

# remove an element
my_set.remove(6)
print(my_set)


#to pop an element
my_set.pop()
print(my_set)   #pops a random element

# to clear  set
my_set.clear()
print(my_set)



#PYTHONS SET OPERATIONS
set_a={1,2,3,4,5}
set_b={4,5,6,7,8}

# Set union 
print(set_a|set_b)
union=(set_a.union(set_b))
print(union)

#set intersection
print(set_a & set_b)
print(set_a.intersection(set_b))

#set difference
print(set_a-set_b)
print(set_a.difference(set_b))

#set symmetric difference ie set of elements in A and B but not in both (excluding the intersection).
print(set_a ^ set_b)
print(set_a.symmetric_difference(set_b))

#set membership test
set_1=set("apple")

print('a'in set_1)
print('p' not in set_1)

#set iterating
for letter in set("apple"):
    print(letter)
    


set1={"k","r","i","t","i","k","a"}
print(set1)

if "r" in set1:
    print("present")
else:
    print("absent")

for i in set1:
    print(f"{i}-->0")

set2={"m","a","h","a","r","s","h","i"}
intersection_set=set1&set2
union_set=set1 | set2
print(f'the union of two sets are: --> {union_set}')
print(f'the intersection of two sets are: --> {intersection_set}')

