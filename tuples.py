tup1=(1,2,3,4)
tup2=(4,5,6,7)
tup3=8,9,10 #tuples can also be formed without using round brackets
tup4=(1,)   #dont forget to give "," if onlhy one element is present
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))
tup5=tup1+tup2+tup3+tup4
print (tup5)

#to access values inside tuples:
# coords1=(13,2,1)
# x=coords1[0]
# y=coords1[1]
# z=coords1[2]
# print(x,y,z)

#tuple destruction

coords=1,2,3
x,y,z=coords
print(x,y,z)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
a, b, c = my_tuple
print(a)
print(b)
print(c)

#nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4


# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')


print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

def sum_and_avg(x, y, z):
    s = x + y + z
    a = s/3
    return(s, a)
(S, A) = sum_and_avg(3, 8, 5)
print('Sum =', S)
print('Avg =', A)




