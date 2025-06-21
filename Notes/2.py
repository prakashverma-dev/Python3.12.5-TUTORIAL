
a = 33
b = 200

if b > a:
    pass
# print("Code Further ie Next Line")


# output = if num%2 == 0 :  "Odd Number"
# print("Output is :", output)

# OR,

# print("Even Number") if num%2 ==0 else print("Odd Number")


# OR, More Shorter -

# num = int(input("Enter the number :"))
# print("Output is :", "Even Number" if num%2 == 0 )


fruits = ["apple", "banana", "graves"]

# # Iterate over List Items -
# for item in fruits:
#   print(item)

# for index, value in enumerate(fruits, 1):
#   print(index) #  0       1      2
#   print(value) # apple banana graves


# my_string = "Hello Papa where are you" #Print first char of each word


text = "Hello World"

i = 0 #indexing of string
while i < len(text):
    print(i) # Will get indexing frm string
    print(text[i]) # Will get the character corresponding to indexing
    i += 1 #Updating the indexing