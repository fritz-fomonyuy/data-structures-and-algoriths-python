fruits= ["mango","avocado","apple","banana"]
numbers=[1,2,3,4,5,6,7,8]

print(sum(numbers))
print(max(numbers))
print(min(fruits))

# bellow is a block of code that takes integer inputs from user stores them in list and calculate their avarage
myList = list()

while (True):
    in_put = input("enter an integer: ")
    if in_put == "done" : break
    value = float(in_put)
    myList.append(value)
    average = sum(myList) / len(myList)
    print("Average: ", average)

#converting strings to list 

sentense = "i am going to the farm"
delimeter = " "
List_sentence = sentense.split(delimeter)
print(List_sentence)
  #reverse the above code block
print(delimeter.join(sentense)) 