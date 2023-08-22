from array import *

arr_1 = array("d", [2.3,3.4,4.5,1.2])


def accessArrElement(array, index):
    """
    Accesses an element in an array based on the given index.

    Parameters:
        array (list): The array or list containing the elements.
        index (int): The index of the element to be accessed.

    Returns:
        None

    Prints the element at the specified index if it exists in the array.
    If the index is out of bounds (greater than or equal to the length of the array),
    it prints a message indicating that the element does not exist.

    Example:
        >>> accessArrElement([10, 20, 30, 40], 2)
        30
        >>> accessArrElement(['a', 'b', 'c'], 5)
        Element does not exist
    """
    if index >= len(array):
        print("Element does not exist")
    else:
        print(array[index])

accessArrElement(arr_1,8)

def searchingElement(array, value):
    """
    Searches for an element in an array and returns its index.

    Parameters:
        array (list): The array or list to be searched.
        value: The element to search for in the array.

    Returns:
        int: The index of the first occurrence of the element in the array, if found.
        str: "Element does not exist in the array" if the element is not found.

    Searches for the specified value in the given array. If the element is found,
    it returns the index of its first occurrence. If the element is not found,
    it returns a string indicating that the element does not exist in the array.

    Example:
        >>> searchingElement([10, 20, 30, 40], 30)
        2
        >>> searchingElement(['a', 'b', 'c'], 'd')
        Element does not exist in the array
    """
    for i in array:
        if i == value:
            return array.index(value)
    return "Element does not exist in the array"
searchingElement(arr_1,2)

     