#create and array and traverse through
from array import *

my_array = array("i",[1,2,3,4,5,6,7,8])
for i in my_array:
    print(i)

#access the first and last element

print(my_array[-1])
print(my_array[0])

#append an element to the array
my_array.append(12)
print(my_array) 
print(my_array.pop()) #last element is removed

#insert value to an array using insert()
my_array.insert(7,20)
print(my_array)

#extend python array using extend() method

my_array1=('i',[1,23,3,4,54])
my_array.extend(my_array1)
print(my_array)

# add items from list to array using fromlist() method
oddnum=[1,3,5,7]
my_array.fromlist(oddnum)
print(my_array)