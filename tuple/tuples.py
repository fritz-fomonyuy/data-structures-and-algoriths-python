new_tuple = (1,"2",2,2,2,3,4,23)
new_tuple1 =  tuple()
print(new_tuple)

#accesing elements of tuple
print(new_tuple[1])
print(new_tuple[:4])

#traversing a tuple
for i in new_tuple:
    print(i)
for i in range(len(new_tuple)):
    print(new_tuple[i])
    
#searching an element in tuple
print(2 in new_tuple) #using in operator returns  true or false

def searchintuple(Tuple,value):
    for i in Tuple:
        if i == value:
            return Tuple.index(i)
    return "element not in tuple"

#more tuple methods

new_tuple.count(2) #returns the number of times an element exist in a tuple
mytuple=tuple([1,2,3,4]) #this methods creates a tuple from a list



