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