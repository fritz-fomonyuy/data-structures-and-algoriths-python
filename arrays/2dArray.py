#create a 2d array to store some random data

import numpy as np

twoDarray = np.array([[1,3,4,5,5],[3,6,7,5,7],[3,5,6,6,3]])
print(twoDarray)

twoDarray1 = np.insert(twoDarray,1,[[13,2,3]], axis=1)
print(twoDarray1)

#accesing 2d array element using a function
def accesElement(array,rowIndex,columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print("incorect index")
    else:
        print(array[rowIndex][columnIndex])

accesElement(twoDarray1,2,5)

#function to traverse 2d array
def traverse2Darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[1][j])

#searching element in 2d array
def searchTDarray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== value:
              return "the value is at index "+str(i)+" "+str(j)
    return "element is not found"
print(searchTDarray(twoDarray,4))

newTdarr = np.delete(twoDarray1,0,axis=0)
print(twoDarray1)