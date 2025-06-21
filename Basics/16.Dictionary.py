'''

#Dictionary : Dictionary Datatype used to store data values in key:value pairs which makes it easier to find values. Dictionaries are written with curly brackets, and have keys-values as its data. Dictionary Key-values are -

Ex: Phone Directory-
        Urvi  : 8827..
        Ravi   : 2344..
        Shyam   : 345...

In Phone Directory, if want to find someone number, I will look through the name, and find the number. 


Similary, In Dictionary we have word-meaning pairs, just like in Phone Directory we have Name-PhoneNo pairs. Thus, whenever we need to store some key-value data then we use dictionary datatype to store.



# Dictionary Key-value Pairs Are -

a) Unindexed : like List and Tuple, Dictionary are not indexed, its unindexed Means Dictionary doesnot have indexing.

b) Ordered : The position we defined key-value pair it will remain same, that order will not change.

c) Changable : Dictionaries are changeable, meaning that we can change, add or remove or update items after the dictionary has been created.

d) Duplicate Keys Not allowed : Dictionaries cannot have two items with the same key, if it so then new key's value overwrite existing key's value.

e) Any Datatype : It can store any datatype like sub-dictionary, list(for multiple storing same datatypes)

'''

# 1. Creating a Dictionary : - It is defined with curly braces{} with key-value pairs as its data, separated by a 'comma'. Where, keys can be strings, numbers,tuples but not lists, sets. and values can be any datatype in the python.

#  Also, Duplicate keys are not allowed and if you assign any duplicate key, then it will overwrite the previous value in the dictionary.

# Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly.

# A dictionary can be created using three ways -

'''

Syntax :
a) using direct key-pair define inside curly braces{} -
dict1 = {

    key1  : value1
    key2  : value2

}

'''

# Ex : dictionary of a phone directory -
phones = {
    "John" : 467555,
    "Ria": 345544,
    "JOy" : 3455455,
    "Ria" : 5533,
    5 : "Hey",
    (1, 3,4) : 3455,
}

# Here, JOhn, Ria, Joy are 'keys' and The attached numbers with them is 'Values'.

# Printing the dict -
print(phones)  

# b)  using empty dictionary -
myDic = {}

myDic["name"] = "Prakash Verma"
myDic["age"] = 24
myDic["DOB"] = "30/12/1997"

print(myDic, type(myDic))

# c) using dict() constructor : Pass many keyword key-value arguments you like, separated by comma: key = value, key = value ...

myDic2 = dict(name = "rohan", age = 23, country = "Norway")

print(myDic2, type(myDic2))


# Checking  type of dictionary -
print(type(phones)) # <class 'dict'>

# Checking the length of dictionary - To determine how many items a dictionary has, use the len() function -
print(len(phones))

# Checking 'keys; exits in dictionay or not :- To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



#2. Accessing Dictionary Items : We can access any value corresponding to key  by using square bracket within existing 'key' name.  OR, with get() method with passing key name.

# Access using key
print(phones[5])
print(phones["John"])

# OR, # Access using get()
print(phones.get(5))
print(phones.get("John"))


# 3. To access all keys and values seperately and in pairs from dictionary : -

#a) To Know the all the keys present in the dictionary : keys() method will return a list of all the keys seperated with comma.

print(phones.keys()) # dict_keys(['John', 'Ria', 'JOy', 5, (1, 3, 4)])

#b) To Know the all the Values present in the dictionary : values() method will return a list of all the values seperated with comma.

print(phones.values()) # dict_values([467555, 5533, 3455455, 'Hey', 3455])

# c) To Know the all the keys-values present in the dictionary in pair : items() method will return each item in a dictionary as pair as tuple in list seperated by comma.
print(phones.items()) # dict_items([('John', 467555), ('Ria', 5533), ('JOy', 3455455), (5, 'Hey'), ((1, 3, 4), 3455)])
 


# 4. Adding/Updating New or Old Dictionary Items : - We can add new key-value pairs or update existing keys by using assignment through referring to its key name OR, using update() method to pass a dictionary, or an iterable object with key:value pairs to update or add dictionary.

#a) Updating Previous Key's value with new value -
phones["John"] = 1233
print(phones)

phones["John"] = 9831 # Get updated Previous Value of this key
print(phones)

# Add a new key-value entry to dict -
phones["kia"] = 727845
print(phones)

#b) using update() method to update a new dictionary key-value pair to existing dict key-value pairs -
more_phones ={
    "kia" : 22332
}
phones.update(more_phones)
print(phones)

#5. Removing Dictionary Items : There are several methods to remove items from a dictionary:

#a)  pop(<pass_key_name>) : To remove the item with the specified key name from dic.
phones.pop("John")  
print(phones)

#b) popitem() :  To remove the last item from dic.
phones.popitem() # to remove last item from dictionary
print(phones)

#c) clear() : To empty the dictionary data completely.

# phones.clear() # empty the dictionary data.
print(phones) # {}

#d) del keyword : To remove the item with the specified key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# NOte: del keyword can also delete the dictionary completely even creation -

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

# print(thisdict) # NameError: name 'thisdict' is not defined



#6. Loopin Through dictionary /Iterating Through a Dictionary : - We can iterate over keys [using keys() method] , values [using values() method] or both [using item() method] with a for loop-in loop -

#In General for-in loop iterate over keys only in dictionary -
for x in phones:
    print(x) # prints all keys in dic
    print(phones[x])  # Prints all value accross keys


# using keys() method to iterate through keys only -
for x in phones.keys():
    print(x)

# using values() method to iterate through values only -
for y in phones.values():
    print(y)

# using items() method to iterate through keys-values both -
for x,y in phones.items():
    print(x)
    print(y)

# using items() to iterate thorugh only keys - (dont pass second variable)
for x in phones.items():
    print(x)     # ('Ria', 5533)



#7. Copy Dictionary :- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2. 

# a) To copy, one way is to use the built-in Dictionary method copy() -
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# b) Another way to make a copy is to use dict() function -

mydict2 = dict(thisdict)
print(mydict2)


#8. Nested Dictionary : When we define a Dictionary INside another dictionary, called nested dictionary - Example1 :

# Area wise phone number differentiation -
phones = {

    "Area1" : {
        "x" : 0,
        "y" :1,
        "z" : 2
    },

    "Area2" : {
        "a" : 3,
        "b" :4,
        "c" : 5
    },

}

# To access Nested Dictionaries items - such as want to access phone number of y -   "y" : 1
print(phones["Area1"]["y"])
print(phones["Area2"]["c"])


# Example2: - Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}



# ------------------------------------------------------------
'''
Example : -

Q1. Given a dictionary in Python, write a Python program to find the
sum of all items in the dictionary.

Input : {'a': 100, 'b':200, 'c':300}
Output : 600
Input : {'x': 25, 'y':18, 'z':45}
Output : 88

'''

def dicSum(dict):

    valueList= []
    for x in dict.values():
        valueList.append(x)

    return sum(valueList) # sum() methods takes iterable object to sum thei items.

Input = {'a': 100, 'b':200, 'c':300}
print(dicSum(Input)) # 600


Input2 = {'x': 25, 'y':18, 'z':45}
print(dicSum(Input2))  # 88



'''
Q2. Given a string and a number N, we need to mirror the characters
from the N-th position up to the length of the string in
alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to
'y', and so on.


Input : N = 3
paradox
output : paizwlc


Input : N = 6
pneumonia
Output : pneumlmrz

# Concept : Mirror Operation : -  a b c d e f .... x y z   
                                  z y x ...        c b a   (Mirror Letter) 

Steps : - i)  Slice the string into two parts: s1= before 'N' position i.e prefix of the string.
          ii) s2 = second string From 'N' Position to till end i.e suffix of the string.
          iii) Do Mirror Operarion of s2 string
          iv) Attach or Concatinate the result of mirror operation with s1
          v) return final string. 


'''

def mirrorFromN(str, N):

    # Slicing string into two parts for mirror operation on second part i.e on suffix -
    prefix = str[0:N-1]
    suffix = str[N-1:]

    # creating a ductionary of a-z with mirror letter corressponding without using zip() method -
    mirror_dic = {}
    for i in range(0, 26):
        alpha = chr(97+i)
        mirrAlpha = chr(122 - i)

        # Assigning key-value pairs 
        mirror_dic[alpha] = mirrAlpha
        
    # Now, Mirror Operation on suffix string -

    mirror_suffix = ""
    for i in range(len(suffix)):
        eachcharacter = suffix[i]
        mirror_suffix += mirror_dic[eachcharacter]

    #Merging Prefix and Mirror Suffix in final string-
    final_str = prefix+mirror_suffix 


    return final_str

strr = "paradox"
N = 3

strr2 = "pneumonia"
N2 = 6
print(mirrorFromN(strr, N)) # output : paizwlc
print(mirrorFromN(strr2, N2)) # output : pneumlmrz


'''
MCQ1 : What will be the output of the following code snippet?

colors = ["red", "green", "burnt sienna", "blue"] 
cotors[2]

What is the output of the colors[2] expression?
a. 'Red
b. It causes a run-time error.
c. 'burnt sienna'  (CORRECT)
d.'green'


MCQ2 : What will be the output of the following code snippet?

colors = ["red", "green", "burnt sienna", "blue"] 
"yellow" in colors

What is the result of the yellow in colors expression?

a. False    (CORRECT)
b. Correct
c. 4
d. ValueError: 'yellow' is not in list




MCQ3 : Square brackets in an assignment statement will create which
type of data structure?

a. List  (CORRECT; l = [])
b. Tuple  (t = ())
c. Set    (s = {} )
d.Dictionary  {d = {}}



MCQ4 :  What type of data is:
arr = [(1,1), (2,2), (3,3), (4,4)]
a. Array of tuples
b. Tuples of lists
c. List of tuples   (CORRECT)
d. Invalid type



MCQ5 : What is the output of the following program ?
print((l, 2) + (3, 4))

a. (1,2), (3,4)
b. (4,6)
c. (1,2,3,4)  ( COREECT : See as two tuples, Concatinate the two tuples with one final tuple )
d. Invalid Syntax






















'''

 










