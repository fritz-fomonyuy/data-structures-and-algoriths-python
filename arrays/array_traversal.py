from array import *

my_array = array('i',[1,2,3,4,5,6,7,8])

def traverseArray(array):
    """
    Visits all the elements of an array.

    Parameters:
       array : the array to be traversed

    Returns:
       The array items

    Example:
       >>> array1 = array("i",[3,4,5,6])
       >>> traverseArray(array1)
           3,4,5,6
    """
    for i in array:
        return(i)

print(traverseArray(my_array))