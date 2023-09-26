import math

def binSearch(arr, value):
    start = 0
    end = len(arr) - 1
    middle = math.floor((start + end) / 2)
    
    while start <= end and not (arr[middle] == value):
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
    
    if arr[middle] == value:
        return middle
    else:
        return -1

sampleArray = [1, 2, 3, 4, 5, 6]
print(binSearch(sampleArray, 3))