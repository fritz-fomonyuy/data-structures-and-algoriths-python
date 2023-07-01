#create dictionary using dick() method
myDict = dict()

word_enc = {"food":"fritz","max":"dog"}

#accesing a dict value we its keys
print(word_enc["food"])

#updating/add an value in dict
word_enc["food"] = 3
print(word_enc)

#traversing a dictionary
def traversing(dict):
    for key in dict:
      print(key, dict)

traversing(word_enc)

def search_dictValue(Dict,value):
    for key in Dict:
        if dict[key] == value:
            return key , value
    return "value not in list"

print(search_dictValue(word_enc,"food"))

#deleting an element from a dict
myDict={1:4,2:3,3:4}
myDict.pop(1)
print(myDict)
myDict.popitem()
print(myDict)
myDict.clear() #deletes the entire dictionary 
del myDict #deletes the entire dictionary