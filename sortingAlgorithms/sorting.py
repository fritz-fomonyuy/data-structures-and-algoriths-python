import math 
def buble_sort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1], customList[j]
    print(customList)

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index],customList[i]
    print(customList)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    return customList
def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        indexPos = math.ceil(j*numberOfBuckets/maxValue)
        arr[indexPos-1].append(j)
    for i in range(numberOfBuckets):
        arr[i]= insertionSort(arr[i])
    h = 0 
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[h]= arr[i][j]
            h +=1
    return customList

def merge(customList,l,m,r):
    n1 = m-l + 1 
    n2 = r - m

    L = [0]* n1
    R = [0]* n2

    for i in range(0 , n1):
        L[i] = customList[l+1]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0 
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <=  R[j]:
            customList[k] = L[i]
        else:
            customList[k] = L[j]
            j+= 1
        k+= 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k+=1

    while j< n2:
        customList = R[j]
        j += 1
        k += 1

def mergeSort(customList,l,r):
    if l < r:
        m = (l+(r-1)//2)  
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList, l,m,r)
    return customList
intergers = [1,5,7,3,8,2,3,7]
buble_sort(intergers)
selectionSort(intergers)
insertionSort(intergers)
bucketSort(intergers)

