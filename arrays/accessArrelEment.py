from array import *

arr_1 = array("d", [2.3,3.4,4.5,1.2])

def accessArrElement(array,index):
    if index > len(array):
        print("element not exist")
    else:
        print(array[index])

accessArrElement(arr_1,8)


def seachingElement(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "element does not exist in the array"

seachingElement(arr_1,)

     