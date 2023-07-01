"""a python program that takes number of days and calculate the average temp """
num_days = int(input("how many days: "))
total = 0 
temp = list()
for i in range(1,num_days+1):
    next_day = int(input("day " + str(i)+"'s high temp:"))
    temp.append(next_day)
    total += next_day
avverage = round(total/num_days,2)
print("\naverage = " + str(avverage))
above = 0
for i in temp:
    if i>avverage:
        above += 1
print(str(above) + "day(s) above average")