import numpy as np

twoDarray = np.array([[1, 3, 4, 5, 5], [3, 6, 7, 5, 7], [3, 5, 6, 6, 3]])
print(twoDarray)

twoDarray1 = np.insert(twoDarray, 0, [[13, 2, 3, 4, 4]], axis=0)
print(twoDarray1)

def accessElement(array, rowIndex, columnIndex):
    """
    Accesses an element in a two-dimensional array based on the given row and column indices.

    Parameters:
        array (ndarray): The two-dimensional array.
        rowIndex (int): The index of the row.
        columnIndex (int): The index of the column.

    Returns:
        None

    Prints the element at the specified row and column indices if they are within the array bounds.
    If the indices are out of bounds, it prints an "Incorrect index" error message.

    Example:
        >>> accessElement(twoDarray1, 2, 3)
        6
    """
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][columnIndex])

accessElement(twoDarray1, 2, 3)


def traverse2Darray(array):
    """
    Traverses a two-dimensional array and prints all its elements.

    Parameters:
        array (ndarray): The two-dimensional array.

    Returns:
        None

    Prints all the elements of the array, row by row.

    Example:
        >>> traverse2Darray(twoDarray1)
        13
        2
        3
        4
        4
        1
        3
        4
        5
        5
        3
        6
        7
        5
        7
        3
        5
        6
        6
        3
    """
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2Darray(twoDarray1)


def search2Darray(array, value):
    """
    Searches for a value in a two-dimensional array and returns its index.

    Parameters:
        array (ndarray): The two-dimensional array to be searched.
        value: The value to search for in the array.

    Returns:
        str: A string indicating the index of the first occurrence of the value in the array, if found.
             If the value is not found, returns "Element is not found".

    Searches for the specified value in the given two-dimensional array.
    If the value is found, it returns a string indicating the index of its first occurrence.
    If the value is not found, it returns a string indicating that the element is not found.

    Example:
        >>> search2Darray(twoDarray, 4)
        'The value is at index 0 2'
    """
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value is at index " + str(i) + " " + str(j)
    return "Element is not found"

print(search2Darray(twoDarray, 4))

newTdarr = np.delete(twoDarray1, 0, axis=0)
print(newTdarr)