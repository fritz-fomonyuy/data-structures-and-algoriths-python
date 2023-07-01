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

#more dictionary methods
my_dict={1:4,2:3,3:4}
dic2 = word_enc.copy() # create coppy of a dictionary

dic3 = {}.fromkeys([1,2,3,4],4)

print(my_dict.get(2,8))
print(my_dict.keys())
print(my_dict.values())

my_dict.setdefault(1,"inserted successfully") #function addes the value automatic when searched and not exist in list

print(my_dict.pop("1","not"))

newdictionary = {23:4,12:2}
my_dict.update(newdictionary)
print(my_dict)