from array import *

my_array = array('i',[1,2,3,4,5,6,7,8])

def traverseArray(array): #fucntion to traverse the array with an iterator 'i'
    for i in array:
        print(i)

traverseArray(my_array)