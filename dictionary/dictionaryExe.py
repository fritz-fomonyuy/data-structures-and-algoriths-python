
word_enc = {"food": "fritz", "max": "dog"}

print(word_enc["food"])

# Updating/adding a value in the dictionary
word_enc["food"] = 3
print(word_enc)

# Traversing a dictionary
def traversing(dict):
    """
    Traverses a dictionary and prints its keys and values.

    Parameters:
        dict (dict): The dictionary to be traversed.

    Returns:
        None

    Prints each key and its corresponding value in the dictionary.

    Example:
        >>> traversing(word_enc)
        food fritz
        max dog
    """
    for key, value in dict.items():
        print(key, value)

traversing(word_enc)


def search_dictValue(Dict, value):
    """
    Searches for a value in a dictionary and returns its corresponding key.

    Parameters:
        Dict (dict): The dictionary to be searched.
        value: The value to search for in the dictionary.

    Returns:
        tuple: A tuple containing the key and value if the value is found.
               If the value is not found, returns "value not in list".

    Searches for the specified value in the given dictionary.
    If the value is found, it returns a tuple containing the key and value.
    If the value is not found, it returns a string indicating that the value is not in the dictionary.

    Example:
        >>> search_dictValue(word_enc, "food")
        ('food', 'fritz')
    """
    for key, val in Dict.items():
        if val == value:
            return key, value
    return "value not in list"

print(search_dictValue(word_enc, "food"))

# Deleting an element from a dictionary
myDict = {1: 4, 2: 3, 3: 4}
myDict.pop(1)
print(myDict)
myDict.popitem()
print(myDict)
myDict.clear()  # Deletes the entire dictionary
del myDict  # Deletes the entire dictionary

# More dictionary methods
my_dict = {1: 4, 2: 3, 3: 4}
dic2 = word_enc.copy()  # Create a copy of a dictionary

dic3 = {}.fromkeys([1, 2, 3, 4], 4)
print(dic3)
print(my_dict.get(2, 8))
print(my_dict.keys())
print(my_dict.values())

my_dict.setdefault(1, "inserted successfully")  # Adds the value automatically when searched and not found in the dictionary

print(my_dict.pop("1", "not"))

new_dictionary = {23: 4, 12: 2}
my_dict.update(new_dictionary)
print(my_dict)