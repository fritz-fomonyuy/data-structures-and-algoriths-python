def mod(interger, cellNum):
    return interger % cellNum

hashValue = mod(56 , 20)
print(hashValue)

def modASCII(string, cellnum):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellnum

hashValue2 = modASCII("fritz", 40)
print(hashValue2)

