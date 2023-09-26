def linearS(arr,value):
    for i in arr:
        if i == value:
            return "value exist"
        else:
            return "value not found"

numbers = [1,2,3,4,5,6,7,8,9]

searchOutput=linearS(numbers,43)
print(searchOutput)