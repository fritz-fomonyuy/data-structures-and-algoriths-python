def buble_sort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1], customList[j]
    print(customList)
intergers = [1,5,7,3,8,2,3,7]
buble_sort(intergers)