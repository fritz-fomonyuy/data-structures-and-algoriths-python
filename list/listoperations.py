names = ["fritz","mark","lafon","fabrice",""]
ages = [1,2,2,4,5,6,12,3]
print(ages)

#access elements in list 
print(ages[3])

#traversing a list 
for b in ages:
    print(b)

for i in range(len(names)):
    names[i] = names[i]+ "34"
    print(names[i])