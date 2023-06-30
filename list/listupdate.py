#update a list element
studentsName = ["fritz","mark"]
print(studentsName)
studentsName[0]="lafon"
print(studentsName)

#insert in list using insert method
studentsName.insert(1,"kongnyuy")
print(studentsName)

#merge two list
books = [1,2,3,4,5]
books.extend(studentsName)
print(books)

#slicing a list
print(books[3:])
cars = [2,3,4,5,3,2]
print(cars[2:])

#delete list element
del books[2:4]
print(books)
books.pop(4)
books.remove("lafon")
print(books)